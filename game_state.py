"""Game state schema and helpers."""

from __future__ import annotations

import copy


DEFAULT_STATS = {
    "swagger": 45,
    "respect": 35,
    "energy": 55,
    "cash": 40,
    "heat": 10,
    "suit": 60,
    "rage": 20,
    "viral": 5,
}


def default_state() -> dict:
    return {
        "scene": "intro",
        "night_id": 1,
        "turn": 0,
        "difficulty": "standard",
        "ui_style": "arcade",
        "streamer_mode": False,
        "stats": copy.deepcopy(DEFAULT_STATS),
        "max_stats": {
            "swagger": 100,
            "respect": 100,
            "energy": 100,
            "cash": 100,
            "heat": 100,
            "suit": 100,
            "rage": 100,
            "viral": 100,
        },
        "inv": {
            "Energy Drink": 1,
            "VIP Card": 0,
            "Fresh Shoes": 0,
            "Silver Chain": 0,
        },
        "flags": {
            "tone_counts": {
                "calm": 0,
                "sarcastic": 0,
                "pleading": 0,
                "heroic": 0,
                "silent": 0,
            },
            "has_white_suit": True,
            "used_gayrutsche": 0,
            "banned_today": False,
            "unlocks": {},
            "viral_clips": [],
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
        "log": [
            "Night 1: Bojan polishes the white suit and heads to the club.",
        ],
        "save_version": 1,
    }


def reset_for_new_run(gs: dict, keep_unlocks: dict | None = None) -> dict:
    unlocks = keep_unlocks or gs.get("flags", {}).get("unlocks", {})
    fresh = default_state()
    fresh["night_id"] = gs.get("night_id", 1) + 1
    fresh["flags"]["unlocks"] = copy.deepcopy(unlocks)
    return fresh
