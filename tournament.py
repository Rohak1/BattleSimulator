from engine import run_game

TOTAL_GAMES = 10

leaderboard = {}

for game in range(TOTAL_GAMES):

    print(f"Running Game {game+1}/{TOTAL_GAMES}")

    players = run_game()

    for player in players:

        if player.name not in leaderboard:
            leaderboard[player.name] = 0

        leaderboard[player.name] += player.score

print("\n==============================")
print("     FINAL LEADERBOARD")
print("==============================\n")

ranking = sorted(
    leaderboard.items(),
    key=lambda x: x[1],
    reverse=True
)

for place, (name, score) in enumerate(ranking, start=1):

    print(
        f"{place:2}. "
        f"{name:<15}"
        f"{score}"
    )