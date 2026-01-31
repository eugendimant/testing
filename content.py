"""Static content tables for the game."""

BOUNCERS = {
    "iron_wall": {
        "id": "iron_wall",
        "name": "Miro 'Iron Wall'",
        "personality": "by-the-book",
        "checks": {
            "min_suit": 55,
            "min_respect": 40,
            "min_viral": None,
            "max_heat": 35,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "calm", "vouch_token": "press", "item": None},
        "dialogue": {
            "greeting": ["Suit check. Respect check. Don't waste my time."],
            "deny": ["No entry. Come back cleaner and calmer."],
            "gayrutsche_line": ["Go cool off on the Gayrutsche slide."],
        },
    },
    "club_historian": {
        "id": "club_historian",
        "name": "Lana 'Records'",
        "personality": "story-driven",
        "checks": {
            "min_suit": 40,
            "min_respect": 30,
            "min_viral": 10,
            "max_heat": 50,
            "requires_item": "Silver Chain",
        },
        "weakness": {"dialogue_tone": "heroic", "vouch_token": "dj", "item": "Silver Chain"},
        "dialogue": {
            "greeting": ["Tell me your story, Serbianhero."],
            "deny": ["Story's weak. No chain, no entry."],
            "gayrutsche_line": ["Slide back down and get your swagger back."],
        },
    },
    "flash": {
        "id": "flash",
        "name": "Viktor 'Flash'",
        "personality": "image-first",
        "checks": {
            "min_suit": 45,
            "min_respect": 25,
            "min_viral": 20,
            "max_heat": 25,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "sarcastic", "vouch_token": "influencer", "item": None},
        "dialogue": {
            "greeting": ["If the crowd isn't filming you, why are you here?"],
            "deny": ["No clip, no entry."],
            "gayrutsche_line": ["Hit the slide and go viral."],
        },
    },
    "night_warden": {
        "id": "night_warden",
        "name": "Nebojsa 'Warden'",
        "personality": "heat-sensitive",
        "checks": {
            "min_suit": 35,
            "min_respect": 50,
            "min_viral": None,
            "max_heat": 20,
            "requires_item": "VIP Card",
        },
        "weakness": {"dialogue_tone": "silent", "vouch_token": "manager", "item": "VIP Card"},
        "dialogue": {
            "greeting": ["Heat's up tonight. Keep it cool."],
            "deny": ["Too hot. Come back tomorrow."],
            "gayrutsche_line": ["Slide away before it gets worse."],
        },
    },
    "heartbeat": {
        "id": "heartbeat",
        "name": "Ana 'Heartbeat'",
        "personality": "empathetic",
        "checks": {
            "min_suit": 30,
            "min_respect": 35,
            "min_viral": None,
            "max_heat": 45,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "pleading", "vouch_token": "friend", "item": None},
        "dialogue": {
            "greeting": ["I can feel your heartbeat from here."],
            "deny": ["Your energy is slipping. Go recharge."],
            "gayrutsche_line": ["Take the slide, breathe, reset."],
        },
    },
}

EVENTS = [
    {
        "id": "street_hawker",
        "title": "Street Hawker",
        "text": "A hawker offers a neon sticker that 'guarantees entry'.",
        "choices": [
            {
                "label": "Buy the sticker (-cash, +swagger)",
                "delta": {"cash": -10, "swagger": 8},
                "effects": ["log:Sticker glows, swagger rises."],
            },
            {
                "label": "Walk away (+energy)",
                "delta": {"energy": 6},
                "effects": ["log:You stay focused and energized."],
            },
        ],
    },
    {
        "id": "street_food",
        "title": "Late-Night Snack",
        "text": "A food cart smells incredible.",
        "choices": [
            {
                "label": "Grab a snack (-cash, +energy, -rage)",
                "delta": {"cash": -8, "energy": 12, "rage": -6},
                "effects": ["log:Carbs calm the chaos."],
            },
            {
                "label": "Keep moving (+respect)",
                "delta": {"respect": 6},
                "effects": ["log:Discipline earns respect."],
            },
        ],
    },
]

QUESTS = [
    {
        "id": "dj_vouch",
        "title": "DJ Favor",
        "setup": "The DJ needs a battery for the mixer.",
        "steps": ["Find a battery in the alley."],
        "choices": [
            {
                "label": "Help the DJ (+respect, +vouch token)",
                "delta": {"respect": 10, "energy": -6},
                "effects": ["vouch:dj", "log:DJ owes you a favor."],
            },
            {
                "label": "Decline (+energy)",
                "delta": {"energy": 6},
                "effects": ["log:You keep your energy for the door."],
            },
        ],
        "reward": {"vouch_token": "dj", "item": None, "delta": {}},
    },
    {
        "id": "press_pass",
        "title": "Press Pass",
        "setup": "A reporter wants a quote from the Serbianhero.",
        "steps": ["Pick a quote."],
        "choices": [
            {
                "label": "Give a heroic quote (+viral, +vouch token)",
                "delta": {"viral": 12, "respect": 4},
                "effects": ["vouch:press", "log:Clip goes viral."],
            },
            {
                "label": "Stay silent (+heat, +swagger)",
                "delta": {"heat": 4, "swagger": 6},
                "effects": ["log:The mystery adds swagger."],
            },
        ],
        "reward": {"vouch_token": "press", "item": None, "delta": {}},
    },
    {
        "id": "friend_ticket",
        "title": "Friend in Line",
        "setup": "An old friend offers a wristband if you cover them.",
        "steps": ["Decide whether to front the cash."],
        "choices": [
            {
                "label": "Cover them (-cash, +vouch token)",
                "delta": {"cash": -12, "respect": 6},
                "effects": ["vouch:friend", "log:Friend slips you a wristband."],
            },
            {
                "label": "Decline (+cash)",
                "delta": {"cash": 6},
                "effects": ["log:You keep your cash for the night."],
            },
        ],
        "reward": {"vouch_token": "friend", "item": None, "delta": {}},
    },
]

MANUAL_PAGES = [
    {
        "id": "manual_calm",
        "title": "Manual: Calm Tone",
        "text": "Calm words lower the Iron Wall's guard. Keep heat under 35.",
        "unlocks": {"new_action": "Scan bouncer", "door_hint": True, "move": None},
    },
    {
        "id": "manual_slide",
        "title": "Manual: Gayrutsche",
        "text": "Sliding reduces heat fast but scuffs your suit. Risk it to reset.",
        "unlocks": {"new_action": "Gayrutsche", "door_hint": False, "move": "Slide Combo"},
    },
    {
        "id": "manual_viral",
        "title": "Manual: Viral Clips",
        "text": "Going viral helps Flash, but too much heat will lock you out.",
        "unlocks": {"new_action": None, "door_hint": True, "move": "Camera Slap"},
    },
]

ENDINGS = [
    {
        "id": "inside",
        "title": "Inside Nachtarena",
        "criteria": ["door_cleared"],
        "text": "The ropes lift. The bass drops. Bojan is finally inside.",
        "badge": "ENTRY",
    },
    {
        "id": "vip_afterparty",
        "title": "VIP Afterparty",
        "criteria": ["door_cleared", "high_swagger"],
        "text": "The VIP manager waves you through to the afterparty.",
        "badge": "VIP",
    },
    {
        "id": "suit_perfect",
        "title": "Suit Perfect",
        "criteria": ["door_cleared", "suit_pristine"],
        "text": "Not a crease on the white suit. Respect earned.",
        "badge": "STYLE",
    },
    {
        "id": "heat_ghost",
        "title": "Heat Ghost",
        "criteria": ["escaped_low_heat"],
        "text": "Bojan vanishes before the heat catches up.",
        "badge": "GHOST",
    },
    {
        "id": "burnout",
        "title": "Total Burnout",
        "criteria": ["burnout"],
        "text": "Energy hits zero. The night ends on the curb.",
        "badge": "BURNOUT",
    },
    {
        "id": "lockdown",
        "title": "Police Lockdown",
        "criteria": ["heat_lockdown"],
        "text": "Sirens flash. Everyone clears out. It's over.",
        "badge": "LOCKDOWN",
    },
]
