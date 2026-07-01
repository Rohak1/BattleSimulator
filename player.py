from config import *

class Player:

    def __init__(self, name, health_pts, attack_pts,
                 critical_pts, heal_pts):

        self.name = name

        # -------------------------
        # Original stat allocation
        # -------------------------
        self.health_pts = health_pts
        self.attack_pts = attack_pts
        self.critical_pts = critical_pts
        self.heal_pts = heal_pts

        # -------------------------
        # Derived values
        # -------------------------

        self.max_health = BASE_HEALTH + health_pts
        self.health = self.max_health

        self.attack_damage = attack_pts * BASE_ATTACK_DAMAGE

        self.critical_damage = (
            CRITICAL_MIN_DAMAGE +
            (critical_pts / 15) *
            (CRITICAL_MAX_DAMAGE - CRITICAL_MIN_DAMAGE)
        )

        self.heal_amount = (
            HEAL_MIN +
            (heal_pts / 15) *
            (HEAL_MAX - HEAL_MIN)
        )

        # -------------------------
        # Match state
        # -------------------------

        self.critical_left = CRITICAL_USES

        self.kills = 0
        self.score = 0

        self.alive = True

        self.allies = set()