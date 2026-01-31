BOUNCERS = [
    {
        "id": "iron_gate",
        "name": "Mika Iron-Gate",
        "personality": "By-the-book and obsessed with dress code.",
        "checks": {
            "min_suit": 6,
            "min_respect": 4,
            "min_viral": None,
            "max_heat": 12,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "calm", "vouch_token": "tailor", "item": "white suit"},
        "dialogue": {
            "greeting": [
                "Suit check. White means white.",
                "You look sharp, but sharp isn't enough.",
            ],
            "deny": [
                "That crease? Not tonight.",
                "Come back when the suit shines.",
            ],
            "gayrutsche_line": ["Maybe slide down the Gayrutsche and cool off."],
        },
    },
    {
        "id": "viral_vet",
        "name": "Lana Clip-Queen",
        "personality": "Lives for viral moments, always scrolling.",
        "checks": {
            "min_suit": 4,
            "min_respect": 3,
            "min_viral": 6,
            "max_heat": 15,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "heroic", "vouch_token": "influencer", "item": "holo wristband"},
        "dialogue": {
            "greeting": ["Give me a reason to record.", "You're trending... or are you?"],
            "deny": ["No buzz, no entry.", "My feed says no."],
            "gayrutsche_line": ["Go slide, maybe someone films it."],
        },
    },
    {
        "id": "heat_hawk",
        "name": "Branko Heat-Hawk",
        "personality": "Smells trouble before it happens.",
        "checks": {
            "min_suit": 3,
            "min_respect": 5,
            "min_viral": None,
            "max_heat": 8,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "silent", "vouch_token": "firewatch", "item": "cooling spray"},
        "dialogue": {
            "greeting": ["Keep it cool.", "Heat stays outside."],
            "deny": ["You're running hot.", "Too much heat tonight."],
            "gayrutsche_line": ["Slide it off, kid."],
        },
    },
    {
        "id": "cashline",
        "name": "Tara Cashline",
        "personality": "Counts every tip and favor.",
        "checks": {
            "min_suit": 4,
            "min_respect": 2,
            "min_viral": None,
            "max_heat": 18,
            "requires_item": "vip voucher",
        },
        "weakness": {"dialogue_tone": "pleading", "vouch_token": "promoter", "item": "vip voucher"},
        "dialogue": {
            "greeting": ["Entry is a balance sheet.", "You look like overhead."],
            "deny": ["Not enough on the table.", "Bring a voucher."],
            "gayrutsche_line": ["Slide away before you go broke."],
        },
    },
    {
        "id": "swaggerwall",
        "name": "Dusan Swaggerwall",
        "personality": "Wants to see bold confidence.",
        "checks": {
            "min_suit": 5,
            "min_respect": 6,
            "min_viral": 3,
            "max_heat": 14,
            "requires_item": None,
        },
        "weakness": {"dialogue_tone": "sarcastic", "vouch_token": "crew", "item": "afterglow cologne"},
        "dialogue": {
            "greeting": ["Show me swagger.", "Make the door believe."],
            "deny": ["Not enough spark.", "Come back with thunder."],
            "gayrutsche_line": ["Slide if you can't stand tall."],
        },
    },
]

QUESTS = [
    {
        "id": "lost_kicks",
        "title": "Lost Kicks",
        "setup": "A dancer lost their rare sneakers backstage.",
        "steps": ["Search the alley", "Return the kicks"],
        "choices": [
            {"label": "Hunt the alley", "delta": {"energy": -10, "respect": 4}, "effects": ["gain_token:crew"]},
            {"label": "Offer cash to a runner", "delta": {"cash": -20, "swagger": 2}, "effects": ["gain_item:white suit"]},
        ],
        "reward": {"vouch_token": "crew", "item": None, "delta": {"respect": 3}},
    },
    {
        "id": "neon_jacket",
        "title": "Neon Jacket",
        "setup": "A promoter needs a neon jacket delivered to the door.",
        "steps": ["Find the jacket", "Deliver it"],
        "choices": [
            {"label": "Borrow from closet", "delta": {"suit": 2, "heat": 2}, "effects": ["gain_token:promoter"]},
            {"label": "Trade a favor", "delta": {"cash": -10, "respect": 2}, "effects": ["gain_item:vip voucher"]},
        ],
        "reward": {"vouch_token": "promoter", "item": None, "delta": {"cash": 10}},
    },
    {
        "id": "cooldown_drink",
        "title": "Cooldown Drink",
        "setup": "A bartender offers a deal: bring ice, get a cooler aura.",
        "steps": ["Grab ice", "Chill out"],
        "choices": [
            {"label": "Sprint for ice", "delta": {"energy": -8, "heat": -6}, "effects": ["gain_item:cooling spray"]},
            {"label": "Negotiate for discount", "delta": {"swagger": 3}, "effects": ["gain_token:firewatch"]},
        ],
        "reward": {"vouch_token": "firewatch", "item": None, "delta": {"heat": -4}},
    },
    {
        "id": "viral_reel",
        "title": "Viral Reel",
        "setup": "A filmmaker wants a 10-second hype clip.",
        "steps": ["Perform the move", "Share the clip"],
        "choices": [
            {"label": "Hero pose", "delta": {"viral": 4, "respect": 2}, "effects": []},
            {"label": "Silent stare", "delta": {"viral": 2, "swagger": 2}, "effects": ["gain_page:manual_silent"]},
        ],
        "reward": {"vouch_token": "influencer", "item": "holo wristband", "delta": {"viral": 2}},
    },
]

MANUAL_PAGES = [
    {
        "id": "manual_silent",
        "title": "Page 03: The Silent Check",
        "text": "When heat is high, silence lowers suspicion. Some bouncers respect a quiet stare.",
        "unlocks": {"new_action": "silent", "door_hint": True, "move": None},
    },
    {
        "id": "manual_slide",
        "title": "Page 07: The Gayrutsche",
        "text": "Sliding resets heat but scuffs the suit. Keep a spare spray handy.",
        "unlocks": {"new_action": "slide", "door_hint": True, "move": None},
    },
    {
        "id": "manual_combo",
        "title": "Page 11: Combo Discipline",
        "text": "Combos build respect fast. Reset by breathing, not by over-slapping.",
        "unlocks": {"new_action": None, "door_hint": False, "move": "roundhouse"},
    },
]

EVENTS = [
    {
        "id": "street_vendor",
        "title": "Street Vendor",
        "text": "A vendor offers neon shades that boost swagger but cost cash.",
        "choices": [
            {"label": "Buy shades", "delta": {"cash": -15, "swagger": 4}, "effects": []},
            {"label": "Walk away", "delta": {"respect": 1}, "effects": []},
        ],
    },
    {
        "id": "fan_gift",
        "title": "Unexpected Fan",
        "text": "Someone recognizes Serbianhero and hands you a wristband.",
        "choices": [
            {"label": "Take wristband", "delta": {"respect": 2, "viral": 2}, "effects": ["gain_item:holo wristband"]},
            {"label": "Decline politely", "delta": {"respect": 1, "heat": -2}, "effects": []},
        ],
    },
]

ENDINGS = [
    {
        "id": "inside_nachtarena",
        "title": "Inside Nachtarena",
        "criteria": ["door_cleared"],
        "text": "The doors swing wide. Bojan steps inside, crowd chanting Serbianhero.",
        "badge": "ENTRY",
    },
    {
        "id": "vip_afterparty",
        "title": "VIP Afterparty",
        "criteria": ["door_cleared", "viral_high"],
        "text": "A VIP wristband glows. You're ushered to the afterparty balcony.",
        "badge": "VIP",
    },
    {
        "id": "suit_perfect",
        "title": "Suit Perfect",
        "criteria": ["door_cleared", "suit_high"],
        "text": "The white suit stays pristine. Mika nods, impressed.",
        "badge": "TAILORED",
    },
    {
        "id": "heat_ghost",
        "title": "Heat Ghost",
        "criteria": ["heat_low", "door_failed"],
        "text": "You fade into the city, heat dropping, planning the next run.",
        "badge": "COOL",
    },
    {
        "id": "total_burnout",
        "title": "Total Burnout",
        "criteria": ["energy_zero"],
        "text": "Energy crashes. Bojan slumps against the rail and resets the night.",
        "badge": "BURNOUT",
    },
    {
        "id": "police_lockdown",
        "title": "Cartoon Lockdown",
        "criteria": ["heat_high"],
        "text": "Sirens flash. The street is locked down in cartoonish chaos.",
        "badge": "LOCKDOWN",
    },
]
