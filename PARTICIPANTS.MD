# Battle Simulator

## Participant Guide

Welcome to the Battle Simulator competition!

In this event, you will design an AI bot that battles against every other participant. Your goal is to earn the highest score across multiple simulated games.

No advanced Python knowledge is required—the challenge is about **strategy**, not programming complexity.

---

# Objective

Create a bot that survives, defeats opponents, and earns the highest tournament score.

Each tournament consists of many matches using the same submitted bots. Scores are accumulated across every match to determine the final leaderboard.

---

# Your Submission

Submit **one Python file** containing a class named `Team.name_School.name`.

Example:

```python
class Bot:
    ...
```

No additional files may be imported (except the provided engine classes).

---

# Required Structure

Every bot **must** define the following:

```python
class Bot:

    NAME = "Example"

    STATS = {
        "health": 5,
        "attack": 5,
        "critical": 5,
        "heal": 5
    }

    FRIENDS = []

    def move(self, state):
        ...
```

---

# Bot Name

```python
NAME = "Knight"
```

Your bot name must be unique.

---

# Stat Distribution

You have **20 points** to distribute.

Maximum in any one stat:

```
15
```

Minimum:

```
0
```

The total **must equal exactly 20**.

Example:

```python
STATS = {
    "health": 6,
    "attack": 7,
    "critical": 5,
    "heal": 2
}
```

---

# Stat Effects

## Health

Starting HP

```
10 + health stat
```

Examples

| Health Stat | Starting HP |
| ----------- | ----------: |
| 0           |          10 |
| 5           |          15 |
| 10          |          20 |
| 15          |          25 |

---

## Attack

Each attack deals

```
Attack × 1.5
```

Examples

| Attack Stat | Damage |
| ----------- | -----: |
| 0           |      0 |
| 4           |      6 |
| 8           |     12 |
| 10          |     15 |
| 15          |   22.5 |

---

## Critical Attack

Each bot has

```
2 Critical Attacks
```

per match.

Critical damage scales between

```
2 → 15
```

depending on your Critical stat.

Higher Critical means stronger burst damage.

---

## Heal

Healing restores between

```
1 → 10 HP
```

depending on your Heal stat.

Healing cannot increase HP above your maximum health.

---

# Teams

Bots may specify teammates.

Example

```python
FRIENDS = [
    "Knight",
    "Medic"
]
```

Teams only exist when **both bots choose each other**.

Example

Knight

```python
FRIENDS = ["Medic"]
```

Medic

```python
FRIENDS = ["Knight"]
```

✓ They become teammates.

If only one bot selects the other, they are treated as enemies.

---

# Free For All

When only a few bots remain alive, the game enters **Free For All**.

During FFA:

* Teams disappear
* Everyone becomes an enemy
* Everyone can attack everyone

The game state tells you when this happens.

---

# The move() Function

Every turn the engine calls

```python
move(state)
```

You must return **exactly one action**.

---

## Basic Attack

```python
from action import Attack

return Attack("EnemyName")
```

---

## Critical Attack

```python
from action import Critical

return Critical("EnemyName")
```

---

## Heal

```python
from action import Heal

return Heal()
```

---

# The State Object

Every turn your bot receives a dictionary.

Example

```python
{
    "turn": 7,

    "ffa": False,

    "me": {
        "name": "Knight",
        "health": 17,
        "max_health": 20,
        "critical_left": 1,
        "kills": 2
    },

    "players": [
        {
            "name": "Medic",
            "health": 15,
            "alive": True,
            "critical_left": 2,
            "is_teammate": True
        },

        ...
    ]
}
```

---

# Available Information

## Me

```python
state["me"]
```

Contains

* name
* current health
* maximum health
* critical attacks remaining
* kills

---

## Players

```python
state["players"]
```

Contains every player in the match.

Each player includes

* name
* health
* alive
* critical_left
* is_teammate

---

## FFA

```python
state["ffa"]
```

Returns

```
True
```

or

```
False
```

---

# Scoring

| Event             | Points |
| ----------------- | -----: |
| Successful Attack |     +1 |
| Kill              |     +3 |
| 1st Survivor      |    +15 |
| 2nd Survivor      |    +14 |

Remaining survivors receive decreasing placement points down to a minimum of **6**.

---

# Invalid Actions

The engine safely ignores:

* attacking yourself
* attacking dead players
* attacking teammates before FFA
* invalid player names
* critical attacks after you've used both

Your bot simply loses that turn.

---

# Tips

Good bots usually:

* Finish weakened enemies.
* Decide when to heal.
* Save critical attacks for important moments.
* Adapt when Free For All begins.
* Avoid wasting turns.

---

# Example Bots

## 1. Berserker

Rushes enemies immediately and spends critical attacks early.

```python
from action import Attack, Critical, Heal

class Bot:

    NAME = "Berserker"

    STATS = {
        "health": 4,
        "attack": 9,
        "critical": 7,
        "heal": 0
    }

    FRIENDS = []

    def move(self, state):

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        enemies.sort(key=lambda x: x["health"])

        target = enemies[0]

        if state["me"]["critical_left"] > 0 and target["health"] < 12:
            return Critical(target["name"])

        return Attack(target["name"])
```

---

## 2. Medic

Heals whenever injured and survives for placement points.

```python
from action import Attack, Critical, Heal

class Bot:

    NAME = "Medic"

    STATS = {
        "health": 8,
        "attack": 3,
        "critical": 2,
        "heal": 7
    }

    FRIENDS = []

    def move(self, state):

        if state["me"]["health"] < state["me"]["max_health"] * 0.8:
            return Heal()

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        enemies.sort(key=lambda x: x["health"])

        return Attack(enemies[0]["name"])
```

---

## 3. Assassin

Saves critical attacks to eliminate weak opponents.

```python
from action import Attack, Critical

class Bot:

    NAME = "Assassin"

    STATS = {
        "health": 3,
        "attack": 5,
        "critical": 12,
        "heal": 0
    }

    FRIENDS = []

    def move(self, state):

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        enemies.sort(key=lambda p: p["health"])

        target = enemies[0]

        if state["me"]["critical_left"] and target["health"] <= 13:
            return Critical(target["name"])

        return Attack(target["name"])
```

---

## 4. Juggernaut

A durable tank that focuses on surviving into the late game.

```python
from action import Attack, Critical, Heal

class Bot:

    NAME = "Juggernaut"

    STATS = {
        "health": 12,
        "attack": 5,
        "critical": 2,
        "heal": 1
    }

    FRIENDS = []

    def move(self, state):

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        if state["me"]["health"] < 8:
            return Heal()

        enemies.sort(key=lambda x: -x["health"])

        if state["ffa"] and state["me"]["critical_left"]:
            return Critical(enemies[0]["name"])

        return Attack(enemies[0]["name"])
```

---

## 5. Opportunist

Targets weak enemies to secure kills, otherwise pressures the strongest opponent.

```python
from action import Attack, Critical, Heal

class Bot:

    NAME = "Opportunist"

    STATS = {
        "health": 6,
        "attack": 7,
        "critical": 3,
        "heal": 4
    }

    FRIENDS = []

    def move(self, state):

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        weak = sorted(enemies, key=lambda x: x["health"])

        if weak[0]["health"] <= 5:
            if state["me"]["critical_left"]:
                return Critical(weak[0]["name"])
            return Attack(weak[0]["name"])

        if state["me"]["health"] < 6:
            return Heal()

        enemies.sort(key=lambda x: -x["health"])

        return Attack(enemies[0]["name"])
```

---

Good luck, and may the smartest strategy win!
