def create_state(current_player, players, turn):

    return {

        "turn": turn,

        "me": {

            "name": current_player.name,
            "health": current_player.health,
            "max_health": current_player.max_health,
            "critical_left": current_player.critical_left,
            "kills": current_player.kills

        },

        "players": [

            {

                "name": p.name,
                "health": p.health,
                "alive": p.alive,
                "critical_left": p.critical_left,
                "is_teammate": (
                    p.name in current_player.allies
                    and
                    current_player.name in p.allies
                )

            }

            for p in players

        ]

    }