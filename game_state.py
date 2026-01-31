from copy import deepcopy

DEFAULT_STATS = {
    "swagger": 5,
    "respect": 4,
    "energy": 20,
    "cash": 30,
    "heat": 5,
    "suit": 8,
    "rage": 2,
    "viral": 3,
}

MAX_STATS = {
    "swagger": 12,
    "respect": 12,
    "energy": 24,
    "cash": 60,
    "heat": 20,
    "suit": 12,
    "rage": 10,
    "viral": 12,
}


def new_game_state():
    return {
        "scene": "intro",
        "night_id": 1,
        "turn": 0,
        "difficulty": "standard",
        "ui_style": "arcade",
        "streamer_mode": False,
        "stats": deepcopy(DEFAULT_STATS),
        "max_stats": deepcopy(MAX_STATS),
        "inv": {},
        "flags": {
            "tone_counts": {"calm": 0, "sarcastic": 0, "pleading": 0, "heroic": 0, "silent": 0},
            "has_white_suit": False,
            "used_gayrutsche": 0,
            "banned_today": False,
            "scans": 0,
            "legacy_boost": False,
        },
        "door": {
            "stage": 0,
            "bouncer_type": "",
            "denied_count": 0,
            "last_denial_reason": [],
        },
        "slap": {
            "combo": 0,
            "objective": 3,
            "last_move": None,
        },
        "quests": {
            "active": [],
            "completed": [],
            "vouch_tokens": {},
        },
        "manual": {
            "pages_found": set(),
        },
        "achievements": {},
        "log": [],
        "save_version": 1,
        "ending": None,
        "ending_summary": [],
    }


def reset_for_new_run(gs):
    gs["scene"] = "hub"
    gs["night_id"] += 1
    gs["turn"] = 0
    gs["stats"] = deepcopy(DEFAULT_STATS)
    gs["max_stats"] = deepcopy(MAX_STATS)
    gs["inv"].clear()
    gs["flags"]["banned_today"] = False
    gs["flags"]["used_gayrutsche"] = 0
    gs["flags"]["scans"] = 0
    gs["door"] = {"stage": 0, "bouncer_type": "", "denied_count": 0, "last_denial_reason": []}
    gs["slap"] = {"combo": 0, "objective": 3, "last_move": None}
    gs["quests"]["active"] = []
    gs["quests"]["completed"] = []
    gs["quests"]["vouch_tokens"] = {}
    gs["manual"]["pages_found"] = set(gs["manual"]["pages_found"])
    gs["log"] = []
    gs["ending"] = None
    gs["ending_summary"] = []
    if gs["flags"].get("legacy_boost"):
        gs["stats"]["respect"] = min(gs["max_stats"]["respect"], gs["stats"]["respect"] + 1)
