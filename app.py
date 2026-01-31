import random

import streamlit as st

from content import BOUNCERS, MANUAL_PAGES, QUESTS
from game_state import new_game_state, reset_for_new_run
from systems import (
    add_log,
    apply_delta,
    clip_event,
    compute_ending,
    door_check,
    gain_item,
    gain_page,
    gain_token,
    get_bouncer,
    pick_bouncer,
    resolve_quest_choice,
    resolve_slide,
    resolve_slap_move,
    roll_event,
    scan_bouncer,
    slap_moves_for_rage,
    summarize_ending,
    update_rage_on_denial,
)
from ui import inject_styles, render_header, render_hud, render_log, render_scene_title


st.set_page_config(page_title="Crimson Corridor: Serbianhero", layout="wide")

inject_styles()

if "gs" not in st.session_state:
    st.session_state["gs"] = new_game_state()


gs = st.session_state["gs"]

render_header(
    "Crimson Corridor: Serbianhero",
    "Bojan fights the line-cutters to reach the midnight club. Build swagger, respect, and viral heat to get inside.",
)

with st.sidebar:
    render_hud(gs)
    st.markdown("---")
    st.markdown("**Manual**")
    pages = gs["manual"]["pages_found"]
    if pages:
        for page_id in sorted(pages):
            page = next((p for p in MANUAL_PAGES if p["id"] == page_id), None)
            if page:
                st.markdown(f"- {page['title']}")
    else:
        st.caption("No manual pages yet.")

    st.markdown("---")
    st.markdown("**Achievements**")
    if gs["achievements"]:
        for achievement in gs["achievements"].values():
            st.markdown(f"- {achievement['title']}")
    else:
        st.caption("None yet.")


col_main, col_side = st.columns([0.68, 0.32])

with col_side:
    render_log(gs)


with col_main:
    if gs["scene"] == "intro":
        render_scene_title("Origin Story")
        st.write(
            "Bojan once ran the door in Novi Sad. When the line-cutters stormed the club, he slapped his way through the chaos."
            " The crowd named him Serbianhero, and tonight he needs to prove it again."
        )
        if st.button("Start Night Run", type="primary"):
            gs["scene"] = "hub"
            pick_bouncer(gs)
            add_log(gs, "Night begins. The club glows in the distance.")

    elif gs["scene"] == "hub":
        render_scene_title("Night Hub")
        st.write("Plan the approach. Gather respect, swag, and leverage before heading to the Nachtarena doors.")

        event = roll_event(gs)
        if event:
            with st.expander(f"Event: {event['title']}"):
                st.write(event["text"])
                for choice in event["choices"]:
                    if st.button(choice["label"], key=f"event-{event['id']}-{choice['label']}"):
                        apply_delta(gs, choice["delta"])
                        gs["turn"] += 1
                        add_log(gs, f"Event resolved: {event['title']}.")

        if not gs["quests"]["active"] and len(gs["quests"]["completed"]) < 2:
            quest = random.choice(QUESTS)
            gs["quests"]["active"] = [quest]

        if gs["quests"]["active"]:
            quest = gs["quests"]["active"][0]
            st.markdown(f"**Quest:** {quest['title']}")
            st.write(quest["setup"])
            for choice in quest["choices"]:
                if st.button(choice["label"], key=f"quest-{quest['id']}-{choice['label']}"):
                    resolve_quest_choice(gs, quest, choice)
                    gs["turn"] += 1

        st.markdown("### Prep Actions")
        if st.button("Polish suit (+Suit, -Cash)"):
            apply_delta(gs, {"suit": 2, "cash": -5})
            add_log(gs, "Suit polished.")
            gs["turn"] += 1
        if st.button("Hype the crowd (+Swagger, +Viral)"):
            apply_delta(gs, {"swagger": 2, "viral": 1})
            add_log(gs, "You feed the hype loop.")
            gs["turn"] += 1
        if st.button("Power nap (+Energy, -Heat)"):
            apply_delta(gs, {"energy": 5, "heat": -2, "rage": -1})
            add_log(gs, "Quick rest brings focus.")
            gs["turn"] += 1

        if st.button("Head to Nachtarena"):
            gs["scene"] = "door_attempt"
            add_log(gs, "You walk toward the rope line.")

    elif gs["scene"] == "door_attempt":
        render_scene_title("Door Attempt")
        bouncer = get_bouncer(gs)
        st.write(random.choice(bouncer["dialogue"]["greeting"]))
        st.markdown(f"**Door stage:** {gs['door']['stage'] + 1}/4")

        st.markdown("**Pick a tone:**")
        tone = st.radio("Tone", ["calm", "sarcastic", "pleading", "heroic", "silent"], horizontal=True)
        st.markdown("".join([f"<span class='tone-pill'>{t}</span>" for t in gs["flags"]["tone_counts"].keys()]), unsafe_allow_html=True)

        col_action1, col_action2, col_action3 = st.columns(3)
        with col_action1:
            if st.button("Speak at the door", type="primary"):
                success, reasons = door_check(gs, tone)
                gs["turn"] += 1
                if success:
                    gs["door"]["stage"] += 1
                    add_log(gs, f"Stage {gs['door']['stage']} cleared.")
                    if gs["door"]["stage"] >= 3:
                        gs["scene"] = "escape_outcome"
                    else:
                        clip_event(gs)
                else:
                    gs["door"]["denied_count"] += 1
                    update_rage_on_denial(gs)
                    add_log(gs, "Denied: " + ", ".join(reasons))
                    add_log(gs, random.choice(bouncer["dialogue"]["gayrutsche_line"]))
                    if gs["door"]["denied_count"] >= 2:
                        gs["scene"] = "slap_chain"

        with col_action2:
            if st.button("Scan the bouncer"):
                scan_bouncer(gs)
                gs["turn"] += 1

        with col_action3:
            if st.button("Walk away + slide"):
                gs["scene"] = "gayrutsche_slide"

        if gs["door"]["last_denial_reason"]:
            st.warning("Denial reasons: " + ", ".join(gs["door"]["last_denial_reason"]))

    elif gs["scene"] == "gayrutsche_slide":
        render_scene_title("Gayrutsche Slide")
        st.write("Security waves you toward the neon slide. One move to reset heat.")
        posture = st.radio("Pick your posture", ["balanced", "wild", "zen"], horizontal=True)
        if st.button("Commit to the slide", type="primary"):
            resolve_slide(gs, posture)
            gs["scene"] = "hub"
            gs["turn"] += 1

    elif gs["scene"] == "slap_chain":
        render_scene_title("Slap Chain")
        st.write("The crowd surges. Bojan chooses how to slap through the line-cutters.")
        st.markdown(f"**Objective slaps remaining:** {gs['slap']['objective']}")
        moves = slap_moves_for_rage(gs["stats"]["rage"])
        if not moves:
            st.info("Rage too low to slap. Try a calmer approach.")
        for move in moves:
            if st.button(move["label"], key=f"slap-{move['id']}"):
                resolve_slap_move(gs, move["id"])
                gs["turn"] += 1
                if gs["slap"]["objective"] <= 0:
                    gs["scene"] = "escape_outcome"

        if st.button("De-escalate and breathe"):
            apply_delta(gs, {"rage": -2, "heat": -1})
            add_log(gs, "You step back from the slap chain.")
            gs["scene"] = "door_attempt"

    elif gs["scene"] == "escape_outcome":
        render_scene_title("Outcome")
        ending = compute_ending(gs)
        gs["ending"] = ending
        gs["ending_summary"] = summarize_ending(gs, ending)
        if ending["id"] in {"inside_nachtarena", "vip_afterparty", "suit_perfect"}:
            gs["flags"]["legacy_boost"] = True
            gs["achievements"][ending["id"]] = {
                "title": ending["title"],
                "desc": ending["text"],
            }
        st.markdown(f"### {ending['title']}")
        st.write(ending["text"])
        st.caption("Badge: " + ending["badge"])
        if st.button("See ending summary"):
            gs["scene"] = "ending_summary"

    elif gs["scene"] == "ending_summary":
        render_scene_title("Night Summary")
        ending = gs.get("ending")
        if ending:
            st.markdown(f"**{ending['title']}**")
        for line in gs.get("ending_summary", []):
            st.write("- " + line)
        if st.button("Restart night"):
            reset_for_new_run(gs)
            pick_bouncer(gs)
            add_log(gs, "Another night, another chance.")

    if gs["stats"]["energy"] <= 0 and gs["scene"] not in {"ending_summary", "escape_outcome"}:
        gs["scene"] = "escape_outcome"

