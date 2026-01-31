"""Streamlit entry point for Bojan's Club Run."""

from __future__ import annotations

import random

import streamlit as st

from crimson_corridor.content import ENDINGS, MANUAL_PAGES, QUESTS
from crimson_corridor.game_state import default_state, reset_for_new_run
from crimson_corridor.systems import (
    add_log,
    apply_delta,
    available_slap_moves,
    award_manual_page,
    choose_bouncer,
    deny_entry,
    door_stage_description,
    evaluate_bouncer,
    evaluate_endings,
    handle_slap,
    increment_turn,
    resolve_gayrutsche,
    roll_event,
    scan_bouncer,
    tone_choice,
    trigger_viral_clip,
)
from crimson_corridor.ui import inject_css, render_hud, render_log, render_scene_card

st.set_page_config(page_title="Crimson Corridor", page_icon="🎧", layout="wide")

if "gs" not in st.session_state:
    st.session_state["gs"] = default_state()

gs = st.session_state["gs"]

inject_css(gs["ui_style"])

st.markdown("<div class='game-title'>Crimson Corridor: Bojan's Club Run</div>", unsafe_allow_html=True)
st.caption("Slap through the line, protect the suit, and reach Nachtarena.")

with st.sidebar:
    st.markdown("### Settings")
    gs["difficulty"] = st.selectbox("Difficulty", ["easy", "standard", "hard"], index=1)
    gs["ui_style"] = st.selectbox("UI Style", ["arcade", "minimal"], index=0)
    gs["streamer_mode"] = st.toggle("Streamer Mode", value=gs["streamer_mode"])
    if st.button("Reset Run", use_container_width=True):
        st.session_state["gs"] = reset_for_new_run(gs)
        st.rerun()

col_main, col_side = st.columns([2.4, 1], gap="large")

with col_side:
    render_hud(gs)
    render_log(gs)


def go_to(scene: str) -> None:
    gs["scene"] = scene


def handle_end_conditions() -> None:
    if gs["stats"]["energy"] <= 0 or gs["stats"]["heat"] >= 90:
        gs["scene"] = "ending_summary"


def record_unlocks() -> None:
    if gs["door"]["stage"] >= 3:
        gs["flags"]["unlocks"]["entry_bonus"] = True
        gs["achievements"]["entry"] = {
            "title": "Inside Nachtarena",
            "desc": "Cleared the door stage for the first time.",
        }


with col_main:
    if gs["scene"] == "intro":
        render_scene_card(
            "How Bojan Became the Serbianhero",
            "Origin Story",
            "Bojan was once a quiet door runner in Novi Sad. When the line-cutters stormed the club, he slapped his way through the chaos to protect the dance floor. Tonight the same crew is back, and getting into the club means everything.",
        )
        if st.button("Start Night", use_container_width=True):
            add_log(gs, "Bojan heads toward Nachtarena." )
            go_to("hub")
            st.rerun()

    elif gs["scene"] == "hub":
        render_scene_card(
            "Street Hub",
            "Choose your next move",
            "Prep for the door, run a quest, or take a risky reset slide.",
        )
        if gs["flags"]["unlocks"].get("entry_bonus"):
            st.success("Unlock active: Entry bonus (+5 respect) this night.")
            gs["flags"]["unlocks"].pop("entry_bonus")
            apply_delta(gs, {"respect": 5})
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("Head to Door", use_container_width=True):
                go_to("door_attempt")
                st.rerun()
        with col_b:
            if st.button("Find a Quest", use_container_width=True):
                quest = next((q for q in QUESTS if q["id"] not in gs["quests"]["completed"]), None)
                if quest:
                    gs["quests"]["active"] = [quest]
                    add_log(gs, f"Quest started: {quest['title']}.")
                    go_to("quest")
                else:
                    add_log(gs, "No new quests tonight.")
                st.rerun()
        with col_c:
            if st.button("Rest & Reset", use_container_width=True):
                apply_delta(gs, {"energy": 10, "heat": -6, "rage": -4})
                add_log(gs, "Bojan catches his breath before the door.")
                increment_turn(gs)
                handle_end_conditions()
                st.rerun()

        st.markdown("---")
        if st.button("Manual", use_container_width=True):
            go_to("manual_view")
            st.rerun()
        if st.button("Achievements", use_container_width=True):
            go_to("achievements_view")
            st.rerun()

    elif gs["scene"] == "quest":
        quest = gs["quests"]["active"][0] if gs["quests"]["active"] else None
        if not quest:
            go_to("hub")
            st.rerun()
        render_scene_card(quest["title"], "Side Quest", quest["setup"])
        for choice in quest["choices"]:
            if st.button(choice["label"], use_container_width=True):
                from crimson_corridor.systems import apply_quest_choice

                apply_quest_choice(gs, quest, choice)
                gs["quests"]["active"] = []
                increment_turn(gs)
                award_manual_page(gs)
                go_to("hub")
                st.rerun()

    elif gs["scene"] == "door_attempt":
        bouncer = choose_bouncer(gs)
        stage = gs["door"]["stage"]
        render_scene_card(
            f"Door Stage {stage + 1}/4",
            door_stage_description(stage),
            f"{bouncer['name']} blocks the way. {random.choice(bouncer['dialogue']['greeting'])}",
        )

        st.markdown("#### Use a vouch token or item")
        tokens = gs["quests"]["vouch_tokens"]
        token_options = [token for token, count in tokens.items() if count > 0]
        if token_options:
            selected = st.selectbox("Vouch token", token_options, key="vouch_token")
            if st.button("Use vouch token", use_container_width=True):
                tokens[selected] -= 1
                add_log(gs, f"Used vouch token: {selected}.")
                apply_delta(gs, {"respect": 6, "heat": -4})
                from crimson_corridor.systems import accept_entry

                accept_entry(gs)
                increment_turn(gs)
                trigger_viral_clip(gs, "Door bypass")
                if gs["door"]["stage"] >= 3:
                    go_to("escape_outcome")
                st.rerun()
        else:
            st.caption("No vouch tokens available yet.")

        items = [item for item, count in gs["inv"].items() if count > 0]
        if items:
            item = st.selectbox("Item", items, key="door_item")
            if st.button("Use item", use_container_width=True):
                gs["inv"][item] -= 1
                add_log(gs, f"Used item: {item}.")
                apply_delta(gs, {"swagger": 4, "respect": 2})
                from crimson_corridor.systems import accept_entry

                accept_entry(gs)
                increment_turn(gs)
                trigger_viral_clip(gs, "Item flex")
                if gs["door"]["stage"] >= 3:
                    go_to("escape_outcome")
                st.rerun()
        st.markdown("---")

        st.markdown("#### Choose your tone")
        tones = ["calm", "sarcastic", "pleading", "heroic", "silent"]
        cols = st.columns(len(tones))
        for tone, col in zip(tones, cols):
            with col:
                if st.button(tone.title(), use_container_width=True):
                    tone_choice(gs, tone)
                    increment_turn(gs)
                    success, reasons = evaluate_bouncer(gs)
                    if success:
                        from crimson_corridor.systems import accept_entry

                        accept_entry(gs)
                        trigger_viral_clip(gs, "Door win")
                    else:
                        deny_entry(gs, reasons)
                        trigger_viral_clip(gs, "Door denial")
                    handle_end_conditions()
                    if gs["door"]["stage"] >= 3:
                        go_to("escape_outcome")
                    st.rerun()

        st.markdown("---")
        if st.button("Scan the bouncer", use_container_width=True):
            scan_bouncer(gs)
            award_manual_page(gs)
            increment_turn(gs)
            st.rerun()
        if st.button("Start slapping", use_container_width=True):
            add_log(gs, "Bojan snaps. The slap chain begins.")
            go_to("slap_chain")
            st.rerun()
        if st.button("Walk away and slide the Gayrutsche", use_container_width=True):
            go_to("gayrutsche_slide")
            st.rerun()

    elif gs["scene"] == "gayrutsche_slide":
        render_scene_card(
            "Gayrutsche Slide",
            "Comedic reset",
            "The bouncers point to the giant neon slide. Choose your posture.",
        )
        if st.button("Tucked Slide", use_container_width=True):
            resolve_gayrutsche(gs, "tucked")
            increment_turn(gs)
            go_to("hub")
            st.rerun()
        if st.button("Showboat Slide", use_container_width=True):
            resolve_gayrutsche(gs, "showboat")
            increment_turn(gs)
            go_to("hub")
            st.rerun()
        if st.button("Safe Slide", use_container_width=True):
            resolve_gayrutsche(gs, "safe")
            increment_turn(gs)
            go_to("hub")
            st.rerun()

    elif gs["scene"] == "slap_chain":
        render_scene_card(
            "Slap Chain",
            "Fight for the line",
            "Build a slap combo to scare the line-cutters away. Rage fuels stronger moves.",
        )
        moves = available_slap_moves(gs)
        for move in moves:
            if st.button(move["name"], use_container_width=True):
                handle_slap(gs, move["name"])
                increment_turn(gs)
                handle_end_conditions()
                if gs["slap"]["combo"] >= gs["slap"]["objective"]:
                    go_to("escape_outcome")
                st.rerun()
        if st.button("De-escalate", use_container_width=True):
            apply_delta(gs, {"heat": -4, "rage": -6})
            add_log(gs, "Bojan steps back before it gets worse.")
            go_to("escape_outcome")
            st.rerun()

    elif gs["scene"] == "escape_outcome":
        render_scene_card(
            "Escape Outcome",
            "The line shifts",
            "You survive the clash. Time to see if the door opens or if the night ends.",
        )
        if st.button("See the outcome", use_container_width=True):
            go_to("ending_summary")
            st.rerun()

    elif gs["scene"] == "ending_summary":
        ending_id = evaluate_endings(gs)
        ending = next(e for e in ENDINGS if e["id"] == ending_id)
        record_unlocks()
        render_scene_card(ending["title"], f"Ending badge: {ending['badge']}", ending["text"])
        st.markdown("#### Viral highlights")
        clips = gs["flags"]["viral_clips"][-3:] or ["No clips caught tonight."]
        for clip in clips:
            st.write(f"• {clip}")
        if st.button("Start new night", use_container_width=True):
            st.session_state["gs"] = reset_for_new_run(gs, gs["flags"].get("unlocks"))
            st.rerun()

    elif gs["scene"] == "manual_view":
        render_scene_card("Security Manual", "Collected hints", "Pages unlock tactics and door secrets.")
        for page in MANUAL_PAGES:
            if page["id"] in gs["manual"]["pages_found"]:
                st.markdown(f"**{page['title']}**")
                st.caption(page["text"])
            else:
                st.caption(f"Locked: {page['title']}")
        if st.button("Back to hub", use_container_width=True):
            go_to("hub")
            st.rerun()

    elif gs["scene"] == "achievements_view":
        render_scene_card("Achievements", "Unlocked feats", "Celebrate Bojan's heroic moments.")
        if not gs["achievements"]:
            st.caption("No achievements yet.")
        for achievement in gs["achievements"].values():
            st.markdown(f"**{achievement['title']}** — {achievement['desc']}")
        if st.button("Back to hub", use_container_width=True):
            go_to("hub")
            st.rerun()

    else:
        go_to("hub")
        st.rerun()

if gs["turn"] > 0 and gs["turn"] % 3 == 0 and gs["scene"] == "hub":
    event = roll_event(gs)
    with col_main:
        st.info(event["text"])
        for choice in event["choices"]:
            if st.button(choice["label"], use_container_width=True):
                apply_delta(gs, choice.get("delta", {}))
                for effect in choice.get("effects", []):
                    if effect.startswith("log:"):
                        add_log(gs, effect.split(":", 1)[1])
                increment_turn(gs)
                st.rerun()
