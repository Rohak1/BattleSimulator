from action import Attack, Critical, Heal

class Bot:

    NAME = "Assassin"

    STATS = {
        "health": 3,
        "attack": 5,
        "critical": 12,
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

        enemies.sort(key=lambda p: p["health"])

        target = enemies[0]

        if state["me"]["critical_left"] and target["health"] <= 13:
            return Critical(target["name"])

        return Attack(target["name"])