"""
Battle Simulator Configuration
All game rules and constants live here.
"""

# -----------------------------
# Stat Allocation Rules
# -----------------------------
TOTAL_STAT_POINTS = 20
MAX_POINTS_PER_STAT = 15

# -----------------------------
# Health
# -----------------------------
BASE_HEALTH = 10          # Health with 0 health points
HEALTH_PER_POINT = 1      # Each health stat point adds 1 HP

# -----------------------------
# Basic Attack
# -----------------------------
BASE_ATTACK_DAMAGE = 1.5  # Damage per attack stat point

# -----------------------------
# Critical Attack
# -----------------------------
CRITICAL_USES = 2

CRITICAL_MIN_DAMAGE = 2   # 0 critical stat
CRITICAL_MAX_DAMAGE = 15  # 15 critical stat

# -----------------------------
# Heal
# -----------------------------
HEAL_MIN = 1              # Heal with 0 heal points
HEAL_MAX = 10             # Heal with 15 heal points

# -----------------------------
# Match Rules
# -----------------------------
FFA_START = 10            # Teams dissolve when this many remain

# -----------------------------
# Scoring
# -----------------------------
ATTACK_SCORE = 1
KILL_SCORE = 3

PLACEMENT_POINTS = {
    1: 15,
    2: 14,
    3: 13,
    4: 12,
    5: 11,
    6: 10,
    7: 9,
    8: 8,
    9: 7,
    10: 5
}

SURVIVORS = 3
PLACEMENT_FIRST = 15
PLACEMENT_LAST = 6