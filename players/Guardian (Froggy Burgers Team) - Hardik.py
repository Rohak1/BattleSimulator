from action import Attack, Heal

class Bot:

    NAME="Guardian"

    STATS={
        "health":8,
        "attack":10,
        "critical":0,
        "heal":2
    }

    FRIENDS=["arceus", "BulwarkV2"]

    def move(self, state):
        me=state["me"]

        # Valid enemy targets
        enemies=[
            p for p in state["players"]
            if p["alive"]
            and p["name"]!=me["name"]
            and (state["ffa"] or not p["is_teammate"])
        ]

        if not enemies:
            return Heal()

        damage=self.STATS["attack"]*1.5

        # Enemies we can eliminate this turn
        killable=[p for p in enemies if p["health"]<=damage]

        # Heal if critical and no kill is available
        if me["health"]<me["max_health"]*0.3 and not killable:
            return Heal()

        # Secure the weakest kill
        if killable:
            target=min(killable, key=lambda p: p["health"])
            return Attack(target["name"])

        # Pressure the weakest enemy while healthy
        if me["health"]>me["max_health"]*0.55:
            target=min(enemies, key=lambda p: p["health"])
            return Attack(target["name"])

        # Recover before re-engaging
        return Heal()
