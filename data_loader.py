import json
from Character_Classes import Saber, Archer, Lancer, Rider, Caster, Assassin, Berserker
from Character_Classes import WeakMinion, MediumMinion, StrongMinion, EasyBoss, MediumBoss, HardBoss

def load_heroes():
    with open("data/heroes.json") as f:
        data = json.load(f)

    class_map = {
        "Saber": Saber,
        "Archer": Archer,
        "Lancer": Lancer,
        "Rider": Rider,
        "Caster": Caster,
        "Assassin": Assassin,
        "Berserker": Berserker
    }

    heroes = []
    for entry in data:
        hero_class = class_map[entry["class"]]
        hero = hero_class(entry["name"])
        heroes.append(hero)
    return heroes

def load_enemies():
    with open("data/enemies.json") as f:
        data = json.load(f)

    enemies_map = {
        "WeakMinion": WeakMinion,
        "MediumMinion": MediumMinion,
        "StrongMinion": StrongMinion,
        "EasyBoss": EasyBoss,
        "MediumBoss": MediumBoss,
        "HardBoss": HardBoss
    }

    enemies = []
    for entry in data:
        enemy_class = enemies_map[entry["class"]]
        enemy = enemy_class(entry["name"])
        enemies.append(enemy)
    return enemies

def save_run_result(result: str):
    with open("data/results.txt", "a") as f:
        f.write(result + "\n")

