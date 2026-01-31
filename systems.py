"""Core mechanics and progression systems."""

from __future__ import annotations

import random

from content import BOUNCERS, EVENTS, MANUAL_PAGES

RAGE_TIERS = {
    "soft": 25,
    "hot": 50,
    "feral": 75,
}

SLAP_MOVES = [
    {"name": "Quick Slap", "min_rage": 0, "delta": {"respect": 4, "heat": 3}},
    {"name": "Double Palm", "min_rage": 25, "delta": {"respect": 6, "heat": 6}},
    {"name": "Heroic Backhand", "min_rage": 50, "delta": {"respect": 9, "heat": 9}},
    {"name": "Serbianhero Spin", "min_rage": 75, "delta": {"respect": 12, "heat": 12}},
]

TONE_EFFECTS = {
    "calm": {"respect": 4, "heat": -3},
    "sarcastic": {"swagger": 6, "heat": 2},
    "pleading": {"respect": 2, "heat": -1, "energy": -2},
    "heroic": {"swagger": 4, "respect": 4, "heat": 1},
    "silent": {"heat": -2, "swagger": 2},
}

VIRAL_EVENTS = [
    {"text": "A clip of the slap goes viral (+viral, +cash, +heat).", "delta": {"viral": 12, "cash": 6, "heat": 5}},
    {"text": "Viewers call it staged (-viral, +respect).", "delta": {"viral": -6, "respect": 4}},
    {"text": "Local blog posts the Serbianhero story (+viral, +swagger).", "delta": {"viral": 8, "swagger": 6}},
]


def clamp(value: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(max_value, value))


def apply_delta(gs: dict, delta: dict) -> None:
    for key, change in delta.items():
        if key in gs["stats"]:
            max_value = gs["max_stats"][key]
            gs["stats"][key] = clamp(gs["stats"][key] + change, 0, max_value)


def add_log(gs: dict, message: str) -> None:
    gs["log"].append(message)


def increment_turn(gs: dict) -> None:
    gs["turn"] += 1


def choose_bouncer(gs: dict) -> dict:
    if not gs["door"]["bouncer_type"]:
        gs["door"]["bouncer_type"] = random.choice(list(BOUNCERS.keys()))
    return BOUNCERS[gs["door"]["bouncer_type"]]


def scan_bouncer(gs: dict) -> str:
    bouncer = choose_bouncer(gs)
    gs["stats"]["energy"] = clamp(gs["stats"]["energy"] - 4, 0, gs["max_stats"]["energy"])
    gs["stats"]["heat"] = clamp(gs["stats"]["heat"] + 2, 0, gs["max_stats"]["heat"])
    hint = f"Scan result: {bouncer['name']} prefers {bouncer['weakness']['dialogue_tone'] or 'silence'} and checks suit/respect."
    add_log(gs, hint)
    return hint


def tone_choice(gs: dict, tone: str) -> None:
    gs["flags"]["tone_counts"][tone] += 1
    apply_delta(gs, TONE_EFFECTS.get(tone, {}))
    add_log(gs, f"Tone chosen: {tone.title()}.")


def _check_item(gs: dict, required: str | None) -> bool:
    if not required:
        return True
    return gs["inv"].get(required, 0) > 0


def evaluate_bouncer(gs: dict) -> tuple[bool, list[str]]:
    bouncer = choose_bouncer(gs)
    reasons = []
    checks = bouncer["checks"]

    if gs["stats"]["suit"] < checks["min_suit"]:
        reasons.append("Suit below requirement")
    if gs["stats"]["respect"] < checks["min_respect"]:
        reasons.append("Respect too low")
    if checks["min_viral"] is not None and gs["stats"]["viral"] < checks["min_viral"]:
        reasons.append("Not viral enough")
    if checks["max_heat"] is not None and gs["stats"]["heat"] > checks["max_heat"]:
        reasons.append("Too much heat")
    if not _check_item(gs, checks["requires_item"]):
        reasons.append("Missing required item")

    weakness = bouncer["weakness"]
    has_token = weakness["vouch_token"] and gs["quests"]["vouch_tokens"].get(weakness["vouch_token"], 0) > 0
    used_item = weakness["item"] and gs["inv"].get(weakness["item"], 0) > 0
    correct_tone = weakness["dialogue_tone"] and gs["flags"]["tone_counts"][weakness["dialogue_tone"]] > 0

    if has_token or used_item or correct_tone:
        if reasons:
            reasons.pop(0)

    return (len(reasons) == 0, reasons)


def deny_entry(gs: dict, reasons: list[str]) -> None:
    bouncer = choose_bouncer(gs)
    gs["door"]["denied_count"] += 1
    gs["door"]["last_denial_reason"] = reasons
    apply_delta(gs, {"rage": 8, "heat": 6, "energy": -4})
    add_log(gs, f"{bouncer['name']} denies entry: {', '.join(reasons)}.")
    add_log(gs, random.choice(bouncer["dialogue"]["deny"]))


def accept_entry(gs: dict) -> None:
    bouncer = choose_bouncer(gs)
    gs["door"]["stage"] += 1
    apply_delta(gs, {"respect": 6, "swagger": 4})
    add_log(gs, f"{bouncer['name']} waves you through stage {gs['door']['stage']}/3.")


def door_stage_description(stage: int) -> str:
    return ["Rope line", "Coat check", "Scanner", "Final door"][stage]


def trigger_viral_clip(gs: dict, reason: str) -> None:
    event = random.choice(VIRAL_EVENTS)
    apply_delta(gs, event["delta"])
    gs["flags"]["viral_clips"].append(f"{reason}: {event['text']}")
    add_log(gs, event["text"])


def handle_slap(gs: dict, move_name: str) -> None:
    move = next((m for m in SLAP_MOVES if m["name"] == move_name), SLAP_MOVES[0])
    apply_delta(gs, move["delta"])
    gs["slap"]["combo"] += 1
    gs["slap"]["last_move"] = move_name
    if gs["slap"]["combo"] >= gs["slap"]["objective"]:
        add_log(gs, "Slap chain objective met. The crowd backs off.")
    trigger_viral_clip(gs, "Slap")


def available_slap_moves(gs: dict) -> list[dict]:
    rage = gs["stats"]["rage"]
    return [move for move in SLAP_MOVES if rage >= move["min_rage"]]


def roll_event(gs: dict) -> dict:
    event = random.choice(EVENTS)
    add_log(gs, f"Event: {event['title']}")
    return event


def award_manual_page(gs: dict) -> dict | None:
    pages = [p for p in MANUAL_PAGES if p["id"] not in gs["manual"]["pages_found"]]
    if not pages:
        return None
    page = random.choice(pages)
    gs["manual"]["pages_found"].add(page["id"])
    add_log(gs, f"Manual page unlocked: {page['title']}")
    return page


def apply_quest_choice(gs: dict, quest: dict, choice: dict) -> None:
    apply_delta(gs, choice.get("delta", {}))
    for effect in choice.get("effects", []):
        if effect.startswith("vouch:"):
            token = effect.split(":", 1)[1]
            gs["quests"]["vouch_tokens"][token] = gs["quests"]["vouch_tokens"].get(token, 0) + 1
        if effect.startswith("log:"):
            add_log(gs, effect.split(":", 1)[1])

    gs["quests"]["completed"].append(quest["id"])


def resolve_gayrutsche(gs: dict, posture: str) -> None:
    gs["flags"]["used_gayrutsche"] += 1
    if posture == "tucked":
        apply_delta(gs, {"heat": -18, "suit": -4, "rage": -6})
        add_log(gs, "You tuck in and slide fast. Heat drops hard.")
    elif posture == "showboat":
        apply_delta(gs, {"heat": -10, "swagger": 8, "suit": -10})
        add_log(gs, "You showboat, tearing the suit but gaining swagger.")
    else:
        apply_delta(gs, {"heat": -14, "energy": 6})
        add_log(gs, "You slide safe and steady, recovering energy.")


def evaluate_endings(gs: dict) -> dict:
    stats = gs["stats"]
    door_cleared = gs["door"]["stage"] >= 3
    if stats["energy"] <= 0:
        return "burnout"
    if stats["heat"] >= 90:
        return "lockdown"
    if door_cleared and stats["swagger"] >= 70:
        return "vip_afterparty"
    if door_cleared and stats["suit"] >= 80:
        return "suit_perfect"
    if door_cleared:
        return "inside"
    if stats["heat"] <= 15:
        return "heat_ghost"
    return "burnout"


def tone_multiplier(gs: dict, tone: str) -> int:
    count = gs["flags"]["tone_counts"].get(tone, 0)
    return 1 if count <= 2 else 2
