# POORLY_BALANCED_BOSS_RAID_GAME
Just a dogshit game

A terminal-based turn-based RPG built in Python as a final project for an Introduction to Python course.
Assemble a team of 3 heroes from 7 Servant classes and fight through 3 stages of escalating difficulty,
facing minions and a powerful boss in each stage.

---

## How to Run

Make sure Python is installed, then run:
py main.py

---

## Gameplay

- Pick a team of 3 heroes from 7 classes: Saber, Archer, Lancer, Rider, Caster, Assassin, Berserker
- Fight through 3 stages, each with 2 minions and a boss
- Use the shared SP system — basic attacks generate SP, skills consume it
- Survive all 3 stages to win

---

## Heroes

| Class | Role | Skill |
|-------|------|-------|
| Saber | Balanced | AOE damage + self shield |
| Archer | DPS | High single target damage |
| Lancer | DPS | Single target, ignores defense |
| Rider | Sustain | AOE damage + self heal |
| Caster | Support | Heals and shields all allies |
| Assassin | Burst | Single target + execute below 10% HP |
| Berserker | Glass cannon | AOE damage, takes 1.5x damage |

---

## Project Structure
├── main.py              — Game loop, team selection, stage progression
├── battle.py            — Turn order, player input, battle loop
├── Character_Classes.py — All character classes and inheritance tree
├── data_loader.py       — File I/O, loads JSON data, saves results
└── data/
├── heroes.json      — Hero roster data
├── enemies.json     — Enemy roster data
└── results.txt      — Run results log (auto-generated)

---

## Advanced Topics

**File I/O** — Hero and enemy data is loaded at runtime from JSON files using Python's `json` module.
Run results are appended to `results.txt` after each session.

**Multidimensional Lists** — The `WAVES` variable in `main.py` is a 2D list where each inner list
represents one stage and contains the enemy names for that stage.

---

## Techniques Used

- Object-Oriented Programming (Classes, Inheritance, Method Overriding)
- `super()` and constructor chaining
- Encapsulation
- File I/O (`json.load()`, `open()` read/write/append)
- Multidimensional Lists
- Lambda functions and `sorted()`
- List comprehensions
- `isinstance()` checks
- `copy.deepcopy()`
- `try/except` error handling
- Random AI (`random.random()`, `random.choice()`)
- F-strings and string formatting
- `enumerate()` and `any()`

---

## Inspired By

- **Fate/Grand Order** — Servant class system and Noble Phantasm skills
- **Honkai: Star Rail** — Turn-based combat, speed-based turn order, shared SP system
- **Tower of Saviors** — Raid-style stage progression with minion + boss formations
