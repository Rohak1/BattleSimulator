import random

from config import (
    FFA_START,
    SURVIVORS,
    PLACEMENT_FIRST,
    PLACEMENT_LAST
)
from helpers import get_player_by_name, are_teammates
from loader import load_bots
from player import Player
from state import create_state
from actions import basic_attack, critical_attack, heal
from action import Attack, Critical, Heal


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
        player.friends = bot.FRIENDS.copy()
        players.append(player)

    turn = 1
    ffa_announced = False

    while True:

        alive_players = [p for p in players if p.alive]

        if len(alive_players) <= SURVIVORS:
            break

        ffa = len(alive_players) <= FFA_START

        if ffa and not ffa_announced:
            print("\n==========================")
            print("   FREE FOR ALL BEGINS")
            print("==========================\n")
            ffa_announced = True

        print(f"\n========== ROUND {turn} ==========\n")

        random.shuffle(alive_players)

        for player in alive_players:

            if not player.alive:
                continue

            state = create_state(
                current_player=player,
                players=players,
                turn=turn,
                ffa=ffa
            )

            action = player.bot.move(state)

            if isinstance(action, Attack):

                target = get_player_by_name(players, action.target)

                if target is None:
                    continue
                if target is player:
                    continue
                if not target.alive:
                    continue
                if are_teammates(player, target, ffa):
                    continue

                result = basic_attack(player, target)

                if result["success"]:
                    print(
                        f"{player.name} attacked {target.name} "
                        f"for {result['damage']:.1f} damage."
                        + (" (KO)" if result["killed"] else "")
                    )

            elif isinstance(action, Critical):

                target = get_player_by_name(players, action.target)

                if target is None:
                    continue
                if target is player:
                    continue
                if not target.alive:
                    continue
                if are_teammates(player, target, ffa):
                    continue

                result = critical_attack(player, target)

                if result["success"]:
                    print(
                        f"{player.name} used a CRITICAL on {target.name} "
                        f"for {result['damage']:.1f} damage."
                        + (" (KO)" if result["killed"] else "")
                    )
                else:
                    print(f"{player.name} tried a critical but had none left.")

            elif isinstance(action, Heal):

                result = heal(player)

                if result["success"]:
                    print(f"{player.name} healed {result['heal']:.1f} HP.")

            # Any other / invalid action is simply ignored (no-op turn).

        turn += 1

    # Get survivors
    survivors = [p for p in players if p.alive]

    # Highest HP gets first place
    survivors.sort(
        key=lambda player: player.health,
        reverse=True
    )

    # Award placement points, counting down from PLACEMENT_FIRST but
    # never going below PLACEMENT_LAST.
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
