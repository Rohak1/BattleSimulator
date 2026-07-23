from action import Attack, Critical, Heal

class Bot:
    NAME = "BulwarkV2"

    STATS = {
        "health": 6,
        "attack": 14,
        "critical": 0,
        "heal":0
    }

    FRIENDS = ["Guardian"]

    def move(self, state):
        me = state["me"]
        ffa = state["ffa"]

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != me["name"]
            and (ffa or not p["is_teammate"])
        ]

        if not enemies:
            return Attack(me["name"])

        attack_damage = self.STATS["attack"] * 1.5

        enemies.sort(key=lambda p: p["health"])
        weakest = enemies[0]
        if weakest["health"] <= attack_damage:
            return Attack(weakest["name"])
        
        enemies.sort(key=lambda p: -p["health"])
        target = enemies[0]

        if ffa:
            target = min(enemies, key=lambda p: p["health"])

        return Attack(target["name"])