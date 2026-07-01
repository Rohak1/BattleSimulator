# Battle Simulator

A customizable AI battle simulator built for a high-school programming competition.

Participants submit a single Python file containing the logic for their bot. The tournament engine loads every submitted bot, runs multiple simulated battles, and ranks participants based on their overall performance.

---

## Current Progress

### ✅ Core Engine

- Basic game engine implemented
- Turn-based battle system
- Automatic bot loading from the `players/` directory
- Tournament runner
- Multiple games can be simulated automatically

---

### ✅ Player System

Each bot has:

- Name
- Health
- Attack
- Critical Attack
- Heal
- Friends (defined before the match)

Every bot also has persistent memory through its class variables, allowing strategies that evolve during a match.

---

### ✅ Stat Distribution

Each bot distributes **20 points** among:

- Health
- Attack
- Critical Attack
- Heal

Current validation rules:

- Total points must equal **20**
- No stat may exceed **15**
- No negative values

---

### ✅ Validation System

Every submitted bot is automatically validated before the tournament starts.

Current checks include:

- NAME exists
- STATS exists
- FRIENDS exists
- move() function exists
- All required stats are present
- Stats are integers
- No negative stats
- Maximum stat limit
- Total stat points = 20

Invalid bots are rejected before the tournament begins.

---

### ✅ Battle Mechanics

Bots currently support:

- Basic Attack
- Critical Attack
- Heal

Each turn, a bot chooses exactly one action.

---

### ✅ Tournament Runner

A tournament runner can execute the same set of bots over multiple games.

Current goal:

- 100 matches
- Aggregate scores across every match
- Produce a final leaderboard

---

### ✅ Survivor System

Matches no longer continue until only one bot remains.

Instead:

- Match ends when only the configured number of survivors remain.
- Remaining bots are ranked by their remaining HP.

Current configuration:

```python
SURVIVORS = 10
```

---

### ✅ Placement Scoring

Survivors receive placement points based on remaining HP.

Current scoring:

| Placement | Points |
|-----------|-------:|
| 1st | 15 |
| 2nd | 14 |
| 3rd | 13 |
| 4th | 12 |
| 5th | 11 |
| 6th | 10 |
| 7th | 9 |
| 8th | 8 |
| 9th | 7 |
| 10th | 6 |

---

## Planned Features

### Team Mode

Bots may define up to five teammates.

Friendships will be **mutual only**.

Example:

Bot A lists Bot B

AND

Bot B lists Bot A

↓

They become teammates.

Otherwise, they are treated as enemies.

---

### Free For All (FFA)

The engine already contains:

```python
FFA_START = 15
```

Once the number of alive bots reaches this threshold:

- Alliances are ignored
- Everyone can attack everyone
- Bots receive information that FFA has begun

---

### Planned Scoring

| Event | Points |
|--------|-------:|
| Successful Attack | +1 |
| Kill | +3 |
| Placement | +6 to +15 |

---

### Future Improvements

- Cannot attack teammates
- Cannot attack dead bots
- Cannot attack yourself
- Ignore invalid actions
- Logging system
- Replay support
- Tournament statistics
- Timeout protection
- Sample bot template
- Helper functions for participants
- Competition documentation

---

## Project Structure

```
BattleSimulator/

├── engine.py
├── tournament.py
├── loader.py
├── validator.py
├── player.py
├── state.py
├── action.py
├── config.py
│
├── players/
│   ├── sample_bot.py
│   ├── bot1.py
│   ├── bot2.py
│   └── ...
│
└── README.md
```

---

## Goal

The objective of this project is to create an easy-to-understand AI programming competition for high-school students, where participants focus on strategy rather than advanced programming concepts.

Each participant submits a single Python file, and the tournament engine automatically evaluates all submissions over multiple simulated games to determine the strongest overall strategy.

---

## Current Status

**Version:** 0.2.0 (In Development)

Core engine is functional, with validation, tournament execution, survivor-based matches, and placement scoring implemented. Team mechanics, FFA transition, and advanced tournament features are currently under development.