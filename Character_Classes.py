import random

class Character:
    def __init__(self, name: str, hp: int, atk: int, defense: int, spd: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd
        self.shield = False

    def is_alive(self) -> bool:
        return self.hp > 0
    
    def take_dmg(self, amount: int) -> int:
        if self.shield:
            self.shield = False
            print(f"{self.name}'s shield blocks the attack!")
            return 0
        actual = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual
    
    def heal(self, amount: int) -> int:
        if self.hp > 0:
            self.hp = min(self.max_hp, self.hp + amount)
            return amount
        return 0
    
    def hp_bar(self) -> str:
        current_hp = int((self.hp / self.max_hp) * 20)
        bar = "█" * current_hp + "░" * (20 - current_hp)
        bar_string = f"{self.name:<30} [{bar}] {self.hp}/{self.max_hp}"
        return bar_string
    
    def basic_attack(self, target):
        actual = target.take_dmg(self.atk)
        return f"{self.name} attacks {target.name} for {actual} damage!"

class Hero(Character):
    def __init__(self, name, hp, atk, defense, spd, skill_name, skill_description):
        super().__init__(name, hp, atk, defense, spd)
        self.skill_name = skill_name
        self.skill_description = skill_description

    def use_skill(self, targets):
        pass

class Enemy(Character):
    def __init__(self, name, hp, atk, defense, spd, skill_name, skill_description):
        super().__init__(name, hp, atk, defense, spd)
        self.skill_name = skill_name
        self.skill_description = skill_description

    def use_skill(self, targets):
        pass

    def choose_action(self, targets):
        living = [h for h in targets if h.is_alive()]
        if not living:
            return "No targets remaining."
        target = random.choice(living)
        return self.basic_attack(target)
        
class Saber(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 1000, atk = 200, defense = 100, spd = 100,
                         skill_name = "Excalibur",
                         skill_description = "Deals AOE damage to all enemies and applies a shield")
        self.description = "A balanced knight. AOE skill that also shields self."
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = target.take_dmg(self.atk)
                results.append(f"{target.name} took {actual} damage")
        self.shield = True
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results) + f", {self.name} is shielded!"
    
class Archer(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 800, atk = 250, defense = 75, spd = 125,
                         skill_name = "Caladbolg",
                         skill_description = "Deals single target damage to an enemy")
        self.description = "A single target sniper. Single target skill with a high multiplier."
        
    def use_skill(self, target):
        actual = target.take_dmg(int(self.atk * 3))
        return f"{self.name} uses {self.skill_name}! {target.name} took {actual} damage"
    
class Lancer(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 1000, atk = 200, defense = 100, spd = 100,
                         skill_name = "Gae Bolg",
                         skill_description = "Deals high single target damage to an enemy; Ignores defense")
        self.description = "A single target fighter. Single target skill that pierces defense."
        
    def use_skill(self, target):
        actual = self.atk * 2
        target.hp = max(0, target.hp - actual)
        return f"{self.name} uses {self.skill_name}! {target.name} took {actual} damage"
    
class Rider(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 1200, atk = 150, defense = 75, spd = 125,
                         skill_name = "Bellerophon",
                         skill_description = "Deals AOE damage to all enemies and heals self by own base attack")
        self.description = "A warrior with a mount. AOE skill that heals self after dealing damage."
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = target.take_dmg(self.atk)
                results.append(f"{target.name} took {actual} damage")
        self.heal(self.atk)
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results) + f", {self.name} is healed!"
    
class Caster(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 800, atk = 150, defense = 75, spd = 75,
                         skill_name = "Luminosité Eternelle",
                         skill_description = "Heals and provides a shield to all allies")
        self.description = "A support specialist. Heals and shields allies with skill."
        
    def use_skill(self, targets):
        for target in targets:
            target.heal(int(self.atk * 2))
            target.shield = True
        return f"{self.name} uses {self.skill_name}! All allies healed for {self.atk * 2} HP and shielded!"

class Assassin(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 600, atk = 300, defense = 50, spd = 150,
                         skill_name = "Zabaniya",
                         skill_description = "Deals single target damage to an enemy and executes them if low hp")
        self.description = "A swift single target executioner. Single target skill that executes enemies below 20% hp."
        
    def use_skill(self, target):
        if target.hp < (target.max_hp * 0.2):
            target.hp = 0
            return f"{self.name} uses {self.skill_name}! {target.name} was executed!"
        actual = target.take_dmg(int(self.atk * 2))
        return f"{self.name} uses {self.skill_name}! {target.name} took {actual} damage"        
        
class Berserker(Hero):
    def __init__(self, name):
        super().__init__(name, hp = 1400, atk = 300, defense = 50, spd = 100,
                         skill_name = "Nine Lives",
                         skill_description = "Deals AOE damage to all enemies")
        self.description = "A glass cannon warrior. Deals increased AOE skill damage but also takes increased damage in return."
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = int(target.take_dmg(self.atk * 1.5))
                results.append(f"{target.name} took {actual} damage")
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results)
    
    def take_dmg(self, amount):
        return super().take_dmg(int(amount * 1.5))
    
class WeakMinion(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 500, atk = 150, defense = 50, spd = 75, skill_name="", skill_description="")

class MediumMinion(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 750, atk = 175, defense = 50, spd = 100, skill_name="", skill_description="")

class StrongMinion(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 1000, atk = 200, defense = 50, spd = 100, skill_name="", skill_description="")

class EasyBoss(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 2000, atk = 200, defense = 50, spd = 70,
                         skill_name = "Fire Ball",
                         skill_description = "Deals AOE damage to all heroes")
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = int(target.take_dmg(self.atk * 1.5))
                results.append(f"{target.name} took {actual} damage")
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results)
    
    def choose_action(self, targets):
        living = [h for h in targets if h.is_alive()]
        if not living:
            return "No targets remaining."
        if random.random() < 0.3:
            return self.use_skill(living)
        else:
            target = random.choice(living)
            return self.basic_attack(target)
        
class MediumBoss(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 2500, atk = 250, defense = 75, spd = 80,
                         skill_name = "Thunder Storm",
                         skill_description = "Deals high AOE damage to all heroes")
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = int(target.take_dmg(self.atk * 2))
                results.append(f"{target.name} took {actual} damage")
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results)
    
    def choose_action(self, targets):
        living = [h for h in targets if h.is_alive()]
        if not living:
            return "No targets remaining."
        if random.random() < 0.3:
            return self.use_skill(living)
        else:
            target = random.choice(living)
            return self.basic_attack(target)
        
class HardBoss(Enemy):
    def __init__(self, name):
        super().__init__(name, hp = 3000, atk = 300, defense = 75, spd = 80,
                         skill_name = "Soul Rend",
                         skill_description = "Deals high AOE damage to all heroes and heals self")
        
    def use_skill(self, targets):
        results = []
        for target in targets:
                actual = int(target.take_dmg(self.atk * 2))
                results.append(f"{target.name} took {actual} damage")
        self.heal(self.atk)
        return f"{self.name} uses {self.skill_name}! " + ", ".join(results) + f", {self.name} heals for {self.atk} HP!"
    
    def choose_action(self, targets):
        living = [h for h in targets if h.is_alive()]
        if not living:
            return "No targets remaining."
        if random.random() < 0.3:
            return self.use_skill(living)
        else:
            target = random.choice(living)
            return self.basic_attack(target)