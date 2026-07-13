from action import Attack, Critical, Heal

class Bot:

    NAME = "Medic"

    STATS = {
        "health": 8,
        "attack": 3,
        "critical": 2,
        "heal": 7
    }

    FRIENDS = []

    def move(self, state):

        me = state["me"]

        if me["health"] < me["max_health"] * 0.8:
            return Heal()

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        enemies.sort(key=lambda x: x["health"])

        return Attack(enemies[0]["name"])