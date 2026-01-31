import random

from content import BOUNCERS, ENDINGS, EVENTS, MANUAL_PAGES, QUESTS


TONE_DELTAS = {
    "calm": {"heat": -1, "respect": 1},
    "sarcastic": {"swagger": 1, "heat": 1},
    "pleading": {"respect": 1, "swagger": -1},
    "heroic": {"respect": 2, "rage": 1},
    "silent": {"heat": -2, "respect": 0},
}

SLAP_MOVES = [
    {"id": "tap", "label": "Tap slap", "rage": 0, "delta": {"respect": 1, "heat": 1}},
    {"id": "cross", "label": "Cross slap", "rage": 3, "delta": {"respect": 2, "heat": 2}},
    {"id": "roundhouse", "label": "Roundhouse slap", "rage": 6, "delta": {"respect": 3, "heat": 3}},
]


def clamp_stat(gs, key):
    gs["stats"][key] = max(0, min(gs["max_stats"][key], gs["stats"][key]))


def apply_delta(gs, delta):
    for key, value in delta.items():
        if key in gs["stats"]:
            gs["stats"][key] += value
            clamp_stat(gs, key)


def add_log(gs, message):
    gs["log"].append(message)


def pick_bouncer(gs):
    bouncer = random.choice(BOUNCERS)
    gs["door"]["bouncer_type"] = bouncer["id"]
    add_log(gs, f"Night {gs['night_id']}: {bouncer['name']} guards the door.")


def get_bouncer(gs):
    for bouncer in BOUNCERS:
        if bouncer["id"] == gs["door"]["bouncer_type"]:
            return bouncer
    return BOUNCERS[0]


def scan_bouncer(gs):
    bouncer = get_bouncer(gs)
    gs["flags"]["scans"] += 1
    cost_heat = 1 + gs["flags"]["scans"]
    apply_delta(gs, {"heat": cost_heat, "energy": -1})
    hint = random.choice(
        [
            f"Scan reveals: weakness tone '{bouncer['weakness']['dialogue_tone']}'.",
            f"Scan reveals: needs min suit {bouncer['checks']['min_suit']}.",
            f"Scan reveals: respects token '{bouncer['weakness']['vouch_token']}'.",
        ]
    )
    add_log(gs, hint)


def roll_event(gs):
    if random.random() < 0.35:
        return random.choice(EVENTS)
    return None


def gain_item(gs, item):
    gs["inv"][item] = gs["inv"].get(item, 0) + 1


def gain_token(gs, token):
    gs["quests"]["vouch_tokens"][token] = gs["quests"]["vouch_tokens"].get(token, 0) + 1


def gain_page(gs, page_id):
    if page_id not in gs["manual"]["pages_found"]:
        gs["manual"]["pages_found"].add(page_id)
        page = next((p for p in MANUAL_PAGES if p["id"] == page_id), None)
        if page:
            add_log(gs, f"Manual page found: {page['title']}")


def apply_effects(gs, effects):
    for effect in effects:
        if effect.startswith("gain_item:"):
            gain_item(gs, effect.split(":", 1)[1])
        if effect.startswith("gain_token:"):
            gain_token(gs, effect.split(":", 1)[1])
        if effect.startswith("gain_page:"):
            gain_page(gs, effect.split(":", 1)[1])


def resolve_quest_choice(gs, quest, choice):
    apply_delta(gs, choice["delta"])
    apply_effects(gs, choice["effects"])
    gs["quests"]["completed"].append(quest["id"])
    gs["quests"]["active"] = []
    add_log(gs, f"Quest complete: {quest['title']}.")


def door_check(gs, tone):
    bouncer = get_bouncer(gs)
    checks = bouncer["checks"]
    reasons = []
    if gs["stats"]["suit"] < checks["min_suit"]:
        reasons.append("Suit isn't sharp enough.")
    if gs["stats"]["respect"] < checks["min_respect"]:
        reasons.append("Respect is too low.")
    if checks["min_viral"] is not None and gs["stats"]["viral"] < checks["min_viral"]:
        reasons.append("Viral buzz is too low.")
    if checks["max_heat"] is not None and gs["stats"]["heat"] > checks["max_heat"]:
        reasons.append("Heat is too high.")
    if checks["requires_item"] and gs["inv"].get(checks["requires_item"], 0) < 1:
        reasons.append("Missing required item.")

    tone_effects = TONE_DELTAS.get(tone, {})
    apply_delta(gs, tone_effects)
    gs["flags"]["tone_counts"][tone] += 1

    token = bouncer["weakness"]["vouch_token"]
    if token and gs["quests"]["vouch_tokens"].get(token, 0) > 0:
        reasons = []
        gs["quests"]["vouch_tokens"][token] -= 1
        add_log(gs, f"Used {token} token to smooth the door.")

    success = len(reasons) == 0
    gs["door"]["last_denial_reason"] = reasons
    return success, reasons


def update_rage_on_denial(gs):
    apply_delta(gs, {"rage": 2, "respect": -1})


def clip_event(gs):
    if random.random() < 0.4:
        roll = random.choice(
            [
                {"viral": 2, "cash": 10, "heat": 1},
                {"viral": -1, "heat": 3},
                {"viral": 3, "respect": 1},
            ]
        )
        apply_delta(gs, roll)
        add_log(gs, f"Clip event: viral shift {roll}.")


def resolve_slide(gs, posture):
    if posture == "balanced":
        apply_delta(gs, {"heat": -12, "suit": -1, "rage": -1})
    elif posture == "wild":
        apply_delta(gs, {"heat": -8, "suit": -3, "respect": 2, "rage": 1})
    else:
        apply_delta(gs, {"heat": -15, "suit": 0, "rage": -2})
    gs["flags"]["used_gayrutsche"] += 1
    add_log(gs, "Gayrutsche slide resolved.")


def slap_moves_for_rage(rage):
    return [move for move in SLAP_MOVES if rage >= move["rage"]]


def resolve_slap_move(gs, move_id):
    move = next((m for m in SLAP_MOVES if m["id"] == move_id), None)
    if not move:
        return
    apply_delta(gs, move["delta"])
    gs["slap"]["combo"] += 1
    gs["slap"]["last_move"] = move["label"]
    gs["slap"]["objective"] = max(0, gs["slap"]["objective"] - 1)
    if gs["slap"]["combo"] % 2 == 0:
        apply_delta(gs, {"swagger": 1})
    clip_event(gs)


def compute_ending(gs):
    criteria = {
        "door_cleared": gs["door"]["stage"] >= 3,
        "door_failed": gs["door"]["stage"] < 3,
        "viral_high": gs["stats"]["viral"] >= 8,
        "suit_high": gs["stats"]["suit"] >= 10,
        "heat_low": gs["stats"]["heat"] <= 4,
        "heat_high": gs["stats"]["heat"] >= 16,
        "energy_zero": gs["stats"]["energy"] <= 0,
    }
    for ending in ENDINGS:
        if all(criteria.get(rule, False) for rule in ending["criteria"]):
            return ending
    return ENDINGS[0]


def summarize_ending(gs, ending):
    summary = []
    if gs["door"]["stage"] >= 3:
        summary.append("Cleared all door stages.")
    else:
        summary.append(f"Stopped at door stage {gs['door']['stage']}.")
    summary.append(f"Final stats: {gs['stats']}.")
    summary.append(f"Manual pages: {len(gs['manual']['pages_found'])}.")
    return summary
