from Character_Classes import Hero, Enemy
from Character_Classes import Saber, Rider, Berserker, Caster  


def get_turn_order(heroes: list, enemies: list) -> list:
    all_characters = heroes + enemies
    turn_order = sorted(all_characters, key = lambda c: c.spd, reverse= True)
    return turn_order

def run_battle(heroes: list, enemies: list, sp: int):
    round_num = 1
    while True:
        if not any(e.is_alive() for e in enemies):
            return True, sp
        if not any(h.is_alive() for h in heroes):
            print("Defeat!")
            return False, sp
        print("-" * 150)
        print(f"ROUND {round_num}")
        print("-" * 150)
        for hero in heroes:
            print(hero.hp_bar())
        print("-" * 150)
        for enemy in enemies:
            if enemy.is_alive():
                print(enemy.hp_bar())
        print("-" * 150)
        turn_order = get_turn_order(heroes, enemies)
        for character in turn_order:
            if not character.is_alive():
                continue
            if isinstance(character, Hero):
                while True:
                    print("-" * 150)
                    print(f"SP: {sp}/3")
                    print("-" * 150)
                    action = input(f"{character.name}'s turn, select an action -> [1. Basic Attack|2. Skill]: ")
                    print("-" * 150)
                    if action == "1":
                        sp = min(3, sp + 1)
                        target = pick_target(enemies)
                        result = character.basic_attack(target)
                        print(result)
                        if not target.is_alive():
                            print(f"{target.name} has been defeated!")
                        if not any(e.is_alive() for e in enemies):
                            break
                        break
                
                    elif action == "2":
                        if sp == 0:
                            print("Not Enough SP!")
                        else:
                            sp -= 1
                            if isinstance(character, (Saber, Rider, Berserker)):
                                alive_before = [e for e in enemies if e.is_alive()]
                                result = character.use_skill(alive_before)
                                print(result)
                                for e in alive_before:
                                    if not e.is_alive():
                                        print(f"{e.name} has been defeated!")
                            elif isinstance(character, Caster):
                                result = character.use_skill([h for h in heroes if h.is_alive()])
                                print(result)
                            else:
                                target = pick_target(enemies)
                                result = character.use_skill(target)
                                print(result)
                                if not target.is_alive():
                                    print(f"{target.name} has been defeated!")

                            if not any(e.is_alive() for e in enemies):
                                break
                            break

                    else:
                        print("Invalid input, choose 1 or 2.")

            elif isinstance(character, Enemy): 
                alive_before = [h for h in heroes if h.is_alive()]
                result = character.choose_action(heroes)
                print(result)
                for hero in alive_before:
                    if not hero.is_alive():
                        print(f"{hero.name} has been defeated!")

            if not any(e.is_alive() for e in enemies):
                break

        round_num += 1

def pick_target(enemies: list):
    living = [e for e in enemies if e.is_alive()]
    for i, enemy in enumerate(living):
        print(f"{i+1}. {enemy.name}")
    while True:
        try:
            print("-" * 150)
            target_choice = int(input("Select Target: "))
            return living[target_choice - 1]
        except (IndexError, ValueError):
            print("Invalid input, choose again.")