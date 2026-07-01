import random

from config import (
    SURVIVORS,
    PLACEMENT_FIRST,
    PLACEMENT_LAST
)
from loader import load_bots
from player import Player
from state import create_state
from actions import basic_attack, critical_attack, heal
from action import (
    Attack,
    Critical,
    Heal
)
def run_game():
    bots = load_bots()

    players = []

    for bot in bots:

        stats = bot.STATS

        player = Player(
            bot.NAME,
            stats["health"],
            stats["attack"],
            stats["critical"],
            stats["heal"]
        )

        player.bot = bot
        player.allies = set(bot.FRIENDS)

        players.append(player)

    turn = 1

    while True:

        alive_players = [p for p in players if p.alive]

        if len(alive_players) <= SURVIVORS:
            break

        print(f"\n========== ROUND {turn} ==========\n")

        random.shuffle(alive_players)

        for player in alive_players:

            if not player.alive:
                continue

            state = create_state(player, players, turn)

            action = player.bot.move(state)

            if isinstance(action, Attack):

                target = next(
                    (p for p in players
                    if p.name == action.target and p.alive),
                    None
                )

                if target:

                    result = basic_attack(player, target)

                    print(
                        f"{player.name} attacked {target.name} "
                        f"for {result['damage']} damage."
                    )

                    if result["killed"]:
                        print(f"{target.name} was eliminated!")

            elif isinstance(action, Critical):

                target = next(
                    (p for p in players
                    if p.name == action.target and p.alive),
                    None
                )

                if target:

                    result = critical_attack(player, target)

                    print(
                        f"{player.name} CRITICAL attacked {target.name} "
                        f"for {result['damage']:.2f} damage."
                    )

                    if result["killed"]:
                        print(f"{target.name} was eliminated!")

            elif isinstance(action, Heal):

                result = heal(player)

                print(
                    f"{player.name} healed "
                    f"{result['heal']} HP."
                )

        turn += 1

    # Get survivors
    survivors = [p for p in players if p.alive]

    # Highest HP gets first place
    survivors.sort(
        key=lambda player: player.health,
        reverse=True
    )

    # Award placement points
    placement_points = PLACEMENT_FIRST

    for player in survivors:

        player.score += placement_points

        if placement_points > PLACEMENT_LAST:
            placement_points -= 1

    return players

if __name__ == "__main__":

    survivors = run_game()

    print("\nSurvivors:\n")

    for player in survivors:
        print(f"{player.name} ({player.health:.1f} HP)")