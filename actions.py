from config import *

def basic_attack(attacker, defender):

    # Can't attack dead players
    if not attacker.alive or not defender.alive:
        return {
            "success": False
        }

    damage = attacker.attack_damage

    defender.health -= damage

    attacker.score += ATTACK_SCORE

    killed = False

    if defender.health <= 0:

        defender.health = 0
        defender.alive = False

        attacker.kills += 1
        attacker.score += KILL_SCORE

        killed = True

    return {
        "success": True,
        "damage": damage,
        "killed": killed
    }

def heal(player):

    if not player.alive:

        return {
            "success": False
        }

    player.health += player.heal_amount

    if player.health > player.max_health:
        player.health = player.max_health

    return {
        "success": True,
        "heal": player.heal_amount
    }

def critical_attack(attacker, defender):

    if not attacker.alive or not defender.alive:

        return {
            "success": False
        }

    if attacker.critical_left == 0:

        return {
            "success": False
        }

    attacker.critical_left -= 1

    damage = attacker.critical_damage

    defender.health -= damage

    attacker.score += ATTACK_SCORE

    killed = False

    if defender.health <= 0:

        defender.health = 0
        defender.alive = False

        attacker.kills += 1
        attacker.score += KILL_SCORE

        killed = True

    return {
        "success": True,
        "damage": damage,
        "killed": killed
    }