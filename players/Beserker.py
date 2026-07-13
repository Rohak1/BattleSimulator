from action import Attack, Critical, Heal

class Bot:

    NAME = "Berserker"

    STATS = {
        "health": 4,
        "attack": 9,
        "critical": 7,
        "heal": 0
    }

    FRIENDS = []

    def move(self, state):

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        enemies.sort(key=lambda x: x["health"])

        target = enemies[0]

        if state["me"]["critical_left"] > 0 and target["health"] < 12:
            return Critical(target["name"])

        return Attack(target["name"])