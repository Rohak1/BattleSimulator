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
SURVIVORS = 2             # Match ends when this many bots remain
FFA_START = 5             # Teams dissolve when this many bots remain

# -----------------------------
# Scoring
# -----------------------------
ATTACK_SCORE = 1
KILL_SCORE = 3

# Placement points count down by 1 from PLACEMENT_FIRST to PLACEMENT_LAST
# as survivors are ranked by remaining HP (1st place gets PLACEMENT_FIRST,
# and the score never drops below PLACEMENT_LAST no matter how many
# survivors there are).
PLACEMENT_FIRST = 15
PLACEMENT_LAST = 6
