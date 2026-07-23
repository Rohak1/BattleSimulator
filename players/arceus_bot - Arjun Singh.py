from action import Attack, Heal

class Bot:
    NAME = "arceus"

    STATS = {
        "health": 10,
        "attack": 10,
        "critical": 0,
        "heal": 0
    }

    FRIENDS = ["Guardian"]

    def __init__(self):
        self.locked_target = None
        self.max_seen_hp = {}
        self.last_turn = None
        self.friends = set()
        self.roster_initialized = False

    def reset(self):
        self.locked_target = None
        self.max_seen_hp = {}
        self.last_turn = None
        self.friends = set()
        self.roster_initialized = False

    def update_friends(self, players):
        if self.roster_initialized:
            return

        names = {
            player.get("name")
            for player in players
        }

        self.friends = {
            friend
            for friend in self.FRIENDS
            if friend in names
        }

        self.roster_initialized = True

    def estimated_attack_upper_bound(self, player):
        name = player.get("name")
        current_hp = player.get("health", 0)
        starting_hp = self.max_seen_hp.get(
            name,
            current_hp
        )

        health_stat = max(0, starting_hp - 10)
        remaining_stat_budget = max(
            0,
            20 - health_stat
        )

        return min(
            15,
            remaining_stat_budget
        )

    def move(self, state):
        me = state["me"]
        players = state["players"]

        my_name = me.get(
            "name",
            self.NAME
        )

        my_hp = me.get(
            "health",
            20
        )

        is_ffa = state.get(
            "ffa",
            False
        )

        turn = state.get(
            "turn"
        )

        match_reset = (
            turn is not None
            and self.last_turn is not None
            and turn < self.last_turn
        )

        if match_reset:
            self.reset()

        self.update_friends(players)

        for player in players:
            name = player.get("name")
            health = player.get(
                "health",
                0
            )

            if (
                name is not None
                and health > self.max_seen_hp.get(
                    name,
                    0
                )
            ):
                self.max_seen_hp[name] = health

        enemies = [
            player
            for player in players
            if (
                player.get(
                    "alive",
                    False
                )
                and player.get(
                    "name"
                ) != my_name
                and (
                    is_ffa
                    or (
                        not player.get(
                            "is_teammate",
                            False
                        )
                        and player.get(
                            "name"
                        ) not in self.friends
                    )
                )
            )
        ]

        if turn is not None:
            self.last_turn = turn

        if not enemies:
            self.locked_target = None
            return Heal()

        my_damage = (
            self.STATS["attack"] * 1.5
        )

        killable_targets = [
            player
            for player in enemies
            if player.get(
                "health",
                0
            ) <= my_damage
        ]

        if killable_targets:
            locked_killable = next(
                (
                    player
                    for player in killable_targets
                    if player.get(
                        "name"
                    ) == self.locked_target
                ),
                None
            )

            if locked_killable is not None:
                target = locked_killable
            else:
                target = max(
                    killable_targets,
                    key=lambda player: (
                        player.get(
                            "health",
                            0
                        ),
                        self.estimated_attack_upper_bound(
                            player
                        )
                    )
                )

            self.locked_target = target["name"]

            return Attack(
                target["name"]
            )

        locked_target = next(
            (
                player
                for player in enemies
                if player.get(
                    "name"
                ) == self.locked_target
            ),
            None
        )

        def target_score(player):
            health = player.get(
                "health",
                0
            )

            max_health = self.max_seen_hp.get(
                player["name"],
                health
            )

            attacks_to_kill = int(
                (
                    health
                    + my_damage
                    - 1
                ) // my_damage
            )

            damage_already_taken = max(
                0,
                max_health - health
            )

            health_after_hit = (
                health - my_damage
            )

            estimated_attack = (
                self.estimated_attack_upper_bound(
                    player
                )
            )

            is_lethal_threat = (
                estimated_attack * 1.5
                >= my_hp
            )

            if is_ffa:
                if (
                    6
                    <= health_after_hit
                    <= 15
                ):
                    execution_setup_rank = 2
                elif health_after_hit <= 5:
                    execution_setup_rank = 0
                else:
                    execution_setup_rank = 1

                return (
                    -attacks_to_kill,
                    execution_setup_rank,
                    damage_already_taken,
                    int(is_lethal_threat),
                    health
                )

            return (
                -attacks_to_kill,
                int(is_lethal_threat),
                estimated_attack,
                damage_already_taken,
                -health
            )

        best_target = max(
            enemies,
            key=target_score
        )

        if locked_target is not None:
            locked_health = locked_target.get(
                "health",
                0
            )

            best_health = best_target.get(
                "health",
                0
            )

            locked_attacks_to_kill = int(
                (
                    locked_health
                    + my_damage
                    - 1
                ) // my_damage
            )

            best_attacks_to_kill = int(
                (
                    best_health
                    + my_damage
                    - 1
                ) // my_damage
            )

            locked_max_health = self.max_seen_hp.get(
                locked_target["name"],
                locked_health
            )

            locked_damage_invested = max(
                0,
                locked_max_health
                - locked_health
            )

            locked_is_hard_committed = (
                locked_health <= my_damage * 2
                and locked_damage_invested >= my_damage
            )

            if locked_is_hard_committed:
                target = locked_target
            elif (
                best_attacks_to_kill >= 3
                and locked_attacks_to_kill
                < best_attacks_to_kill
            ):
                target = locked_target
            elif (
                best_attacks_to_kill
                < locked_attacks_to_kill
            ):
                target = best_target
            else:
                target = locked_target
        else:
            target = best_target

        target_name = target.get(
            "name"
        )

        if (
            target_name is None
            or target_name == my_name
            or not target.get(
                "alive",
                False
            )
            or (
                not is_ffa
                and (
                    target.get(
                        "is_teammate",
                        False
                    )
                    or target_name in self.friends
                )
            )
        ):
            target = max(
                enemies,
                key=target_score
            )

            target_name = target["name"]

        self.locked_target = target_name

        return Attack(
            target_name
        )
