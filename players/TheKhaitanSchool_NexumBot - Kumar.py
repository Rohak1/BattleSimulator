from action import Attack, Heal

class Bot:
    NAME = "ZZ_NexumBot"
    
    STATS = {
        "health": 5,
        "attack": 15,
        "critical": 0,
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

        if not enemies:
            return Heal()

        killable = [e for e in enemies if e["health"] <= 22.5]

        if killable:
            killable.sort(key=lambda x: (-x["health"], x["name"]))
            return Attack(killable[0]["name"])
        
        if state["turn"] > 50:
            enemies.sort(key=lambda x: -x["health"])
            return Attack(enemies[0]["name"])

        return Heal()
