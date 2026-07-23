from action import Attack, Critical, Heal

class DominanceEngine3:
    NAME = "DominanceEngine3"
    STATS = {"health": 5, "attack": 15, "critical": 0, "heal": 0}
    FRIENDS = []

    def move(self, state):
        me = state["me"]
        if "calc_values" in me:
            my_dmg = me["calc_values"]["attack"]
        elif "expected_damage" in me:
            my_dmg = me["expected_damage"]["attack"]
        else:
            my_dmg = self.STATS["attack"] * 1.5

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p.get("is_teammate", False))
        ]

        if not enemies:
            return Heal()

        killable = [p for p in enemies if p["health"] <= my_dmg]
        if killable:
            killable.sort(key=lambda p: p["health"], reverse=True)
            return Attack(killable[0]["name"])

        enemies.sort(key=lambda p: p["health"])
        return Attack(enemies[0]["name"])
