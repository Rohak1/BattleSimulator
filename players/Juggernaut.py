from action import Attack, Critical, Heal

class Bot:

    NAME = "Juggernaut"

    STATS = {
        "health": 12,
        "attack": 5,
        "critical": 2,
        "heal": 1
    }

    FRIENDS = []

    def move(self, state):

        me = state["me"]

        alive = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        if me["health"] < 8:
            return Heal()

        alive.sort(key=lambda x: -x["health"])

        strongest = alive[0]

        if state["ffa"] and state["me"]["critical_left"]:
            return Critical(strongest["name"])

        return Attack(strongest["name"])