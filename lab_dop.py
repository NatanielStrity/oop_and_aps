import random as r


class Creature:
    """Базовый класс для всех существ."""
    
    def __init__(self, name, base_health, base_attack, base_defense):
        self.name = name                  # Имя существа
        self.base_health = base_health    # Базовое здоровье
        self.base_attack = base_attack     # Базовая атака
        self.base_defense = base_defense   # Базовая защита
        self.count = 1                    # Количество существ

    def spawn(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        """Метод атаки другой сущности."""
        damage = max(0, self.total_attack() - other.total_defense())
        print(f"{self.name} атакует {other.name} на {damage} урона!")
        other.take_damage(damage)

    def take_damage(self, damage):
        """Метод получения урона."""
        if damage > 0:
            health_after_damage = self.total_health() - damage
            count_after_damage = self.count() - (self.total_attack // self.base_health)
            if health_after_damage > 0:
                print(f"{self.name} теряет {damage} здоровья. Осталось существ в отряде {count_after_damage}. Общее здоровье отряда: {health_after_damage}.
            else:
                print(f"{self.name} погибает.")
        else:
            print(f"Атака {self.name} не нанесла урона.")


class Peasant(Creature):

    def __init__(self, name):
        self.name = name
        self.base_health = 3                # Базовое здоровье
        self.base_attack = 1                # Базовая атака (тип 1)
        self.base_defense = 1               # Базовая защита
        self.count = 1                      # Количество существ

    def spawn(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name}: Удар вилами!")
        super().attack(other)

        

class Archer(Creature):

    def __init__(self, name):
        self.name = name
        self.base_health = 7
        self.base_attack = r.randint(2, 4)
        self.base_defense = 3
        self.count = 1

    def spawn(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense
    
    def attack(self, other):
        print(f"{self.name}: Выстрел из лука!")
        super().attack(other)


class Footman(Creature):

    def __init__(self, name):
        self.name = name
        self.base_health = 16
        self.base_attack = r.randint(2, 4)
        self.base_defense = 8
        self.count = 1

    def spawn(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name}: Удар мечом!")
        super().attack(other)


class  Priest(Creature):

    def __init__(self, name):
        self.name = name
        self.base_health = 54
        self.base_attack = r.randint(9, 12)
        self.base_defense = 12
        self.count = 1

    def spawn(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name}: Магический удар!")
        super().attack(other)


k = Peasant('Крестьянин')
l = Archer('Лучник')
t = Footman('Мечник')
m = Priest('Монах')


k.spawn(100)
l.spawn(100)
k.attack(l)
k.attack(l)
k.attack(l)
k.attack(l)
