from action import Attack, Heal, Critical
import random


class Bot:

    NAME = "Bot_2"

    STATS = {
        "health": 5,
        "attack": 5,
        "critical": 5,
        "heal": 5
    }

    FRIENDS = []

    def move(self, state):

        enemies = []

        for player in state["players"]:

            if (
                player["alive"]
                and not player["is_teammate"]
                and player["name"] != state["me"]["name"]
            ):
                enemies.append(player)

        # Heal if health is low
        if state["me"]["health"] <= 5:
            return Heal()

        if len(enemies) == 0:
            return Heal()

        target = random.choice(enemies)

        # Randomly decide whether to use critical
        if (
            state["me"]["critical_left"] > 0
            and random.random() < 0.20
        ):
            return Critical(target["name"])

        return Attack(target["name"])