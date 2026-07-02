def get_player_by_name(players, name):
    """
    Returns the player object with the given name.
    Returns None if no such player exists.
    """

    for player in players:
        if player.name == name:
            return player

    return None


def are_teammates(player1, player2, ffa=False):
    """
    Returns True only if both players mutually selected
    each other as friends and FFA has not started.
    """

    if ffa:
        return False

    return (
        player2.name in player1.friends and
        player1.name in player2.friends
    )