from config import TOTAL_STAT_POINTS, MAX_POINTS_PER_STAT


def validate_bot(bot):

    if not hasattr(bot, "NAME"):
        raise Exception("Bot has no NAME")

    if not hasattr(bot, "STATS"):
        raise Exception(f"{bot.NAME} has no STATS")

    stats = bot.STATS

    required = [
        "health",
        "attack",
        "critical",
        "heal"
    ]

    for stat in required:

        if stat not in stats:
            raise Exception(f"{bot.NAME} missing {stat}")

        if not isinstance(stats[stat], int):
            raise Exception(f"{bot.NAME}: {stat} must be integer")

        if stats[stat] < 0:
            raise Exception(f"{bot.NAME}: {stat} cannot be negative")

        if stats[stat] > MAX_POINTS_PER_STAT:
            raise Exception(
                f"{bot.NAME}: {stat} exceeds max points"
            )

    total = sum(stats.values())

    if total != TOTAL_STAT_POINTS:

        raise Exception(
            f"{bot.NAME}: total stat points must equal {TOTAL_STAT_POINTS}"
        )

    if not hasattr(bot, "FRIENDS"):
        raise Exception(f"{bot.NAME} missing FRIENDS")

    if not isinstance(bot.FRIENDS, list):
        raise Exception("FRIENDS must be a list")

    if not hasattr(bot, "move"):
        raise Exception(f"{bot.NAME} missing move()")