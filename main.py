import copy
from data_loader import load_heroes, load_enemies, save_run_result
from battle import run_battle

WAVES = [
    ["Goblin", "Goblin", "Saruman The Goblin King"],      # Stage 1
    ["Hellhound", "Hellhound", "Fenrir The Devourer"],    # Stage 2
    ["Death Knight", "Death Knight", "Odin The Undying"], # Stage 3
]

def main():
    sp = 2
    team = []
    heroes = load_heroes()
    enemies = load_enemies()

    print("-" * 150)
    print("WELCOME TO POORLY_BALANCED_BOSS_RAID GAME | INTERACT USING NUMBER KEYS 1-3")
    print("-" * 150)
    print("SELECT YOUR TEAM OF 3 HEROES | TYPE IN THE HERO NUMBER ONLY")
    print("-" * 150)

    for i, hero in enumerate(heroes):
        print(f"{i+1}. {hero.name} [{hero.__class__.__name__}]")
        print(f"   {hero.description}")
        
    print("-" * 150)

    for slot in range(3):
        while True:
            try:
                choice = int(input(f"Pick hero {slot+1}/3: "))
                picked = heroes[choice - 1]
                print(f"Selected: {picked.name} [{picked.__class__.__name__}]")
                if picked in team:
                    print("Already picked, choose another.")
                else:
                    team.append(picked)
                    break
            except (IndexError, ValueError):
                print("Invalid input, try again.")

    for stage_index, wave in enumerate(WAVES):
        print("-" * 150)
        print(f"Stage {stage_index + 1}. Defeat all enemies.")
        print("-" * 150)
        stage_enemies = []
        counts = {}
        for name in wave:
            for e in enemies:
                if e.name == name:
                    fresh = copy.deepcopy(e)
                    counts[name] = counts.get(name, 0) + 1
                    if wave.count(name) > 1:
                        fresh.name = f"{name} {counts[name]}"
                    stage_enemies.append(fresh)
                    break
        result, sp = run_battle(team, stage_enemies, sp)
        if not result:
            print("Defeat")
            save_run_result("Defeat")
            return
        if stage_index == len(WAVES) - 1:
            print("Victory! All bosses defeated. Game Clear!")
        else:
            print(f"Victory! Stage {stage_index + 1} cleared!")
            for hero in team:
                if hero.is_alive():
                    hero.heal(int(hero.max_hp * 0.3))
            print("Your team recovers 30% HP before the next stage.")
    save_run_result("Victory")

if __name__ == "__main__":
    main()