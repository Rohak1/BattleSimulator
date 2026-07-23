from action import Attack, Critical, Heal


class Bot:

    NAME = "Ashray"

    STATS = {
        "health": 8,
        "attack": 11,
        "critical": 0,
        "heal": 1
    }

    FRIENDS = []

    def __init__(self):
        self.previoushp = {}
        self.previouscrits = {}

    def move(self, state):
        myhp = state["me"]["health"]
        crits_left = state["me"]["critical_left"]
        mydam = self.STATS["attack"] * 1.5

        for p in state["players"]:
            pname = p["name"]
            php = p["health"]
            pcrits = p.get("critical_left", 2)

            self.previoushp[pname] = php
            self.previouscrits[pname] = pcrits

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p.get("is_teammate", False))
        ]

        if not enemies:
            return Heal()

        enemies.sort(key=lambda p: p["health"])
        
        target = enemies[0]
        
        if len(enemies) > 1 and target["health"] <= 3:
            target = enemies[1]

        if target["health"] < 2 and crits_left > 0:
            return Critical(target["name"])

        return Attack(target["name"])
