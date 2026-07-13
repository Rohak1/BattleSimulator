from action import Attack, Critical, Heal

class Bot:

    NAME = "Opportunist"

    STATS = {
        "health": 6,
        "attack": 7,
        "critical": 3,
        "heal": 4
    }

    FRIENDS = []

    def move(self, state):

        me = state["me"]

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        weak = sorted(enemies, key=lambda x: x["health"])

        if weak[0]["health"] <= 5:
            if me["critical_left"]:
                return Critical(weak[0]["name"])
            return Attack(weak[0]["name"])

        if me["health"] < 6:
            return Heal()

        enemies.sort(key=lambda x: -x["health"])

        return Attack(enemies[0]["name"])