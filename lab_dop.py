import random as r


class Hero:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

    def magic_cast(self, spell):
        if spell == "Каменная Кожа" and self.mana >= 10:
            self.mana -= 10
            buf_d = 12
            return buf_d  # Увеличение защиты
        elif spell == "Божественная сила" and self.mana >= 15:
            self.mana -= 15
            buf_a = 5
            return buf_a  # Увеличение атаки
        else:
            print("Недостаточно маны или неправильное заклинание.")
            return 0
    
    def info(self):
        return print(f"Текущий уровень маны Героя {self.name}: {self.mana}")
        


class Creature():
    def __init__(self, name, health, defense, damage):
        self.name = name
        self.health = health
        self.defense = defense
        self.damage = damage
        self.count = 0

    def spawn(self, n):
        self.count += n

    def total_health(self):
        return self.health * self.count

    def total_damage(self):
        return self.damage * self.count

    def attack(self, other):
        damage_dealt = max(0, self.total_damage() - other.defense)
        print(f"{self.name} атакует {other.name} на {damage_dealt} урона!")
        other.take_damage(damage_dealt)

    def retaliatory_attack(self, other):
        self.damage_dealt = max(0, self.total_damage()*0.75 - other.defense)
        print(f"{self.name} дает отпор {other.name} на {self.damage_dealt} урона!")
        other.take_damage(self.damage_dealt)

    def take_damage(self, damage):
        if damage > 0:
            self.count -= damage // self.health
            print(f"{self.name} теряет {damage} здоровья. Осталось существ в отряде {self.count}. Общее здоровье отряда: {self.total_health()}.")
        if self.count < 0:
            self.count = 0

    def is_alive(self):
        return self.count > 0

    def status(self):
        return print(f"{self.name}: {self.count} (Здоровье: {self.total_health()})")


class Peasant(Creature):
    def __init__(self):
        super().__init__("Крестьяне", health=3, defense=1, damage=1)

    
    def pitchfork_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(Peasant)
    
    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


class Archer(Creature):
    def __init__(self):
        super().__init__("Лучники", health=7, defense=3, damage=r.randint(2, 4))

    def archery(self, other):
        super().attack(other = other)
        other.retaliatory_attack(Archer)
    
    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


class Footman(Creature):
    def __init__(self):
        super().__init__("Мечники", health=16, defense=8, damage=r.randint(2, 4))


class Priest(Creature):
    def __init__(self):
        super().__init__("Монахи", health=54, defense=12, damage=r.randint(9, 12))


if __name__ == "__main__":

    hero = Hero('Писюньчик', 100)
    peasants = Peasant()
    archers = Archer()
    footman = Footman()
    priest = Priest()


    
    hero.magic_cast("Каменная Кожа")
    #peasants.spawn(10)
    #archers.spawn(5)

    #peasants.attack(archers)
    #peasants.attack(archers)

    
    #archers.status()