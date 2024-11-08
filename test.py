'''Это мини-игра была сделана на основе серии игр Heroes of Might and Magic
    
   Есть 4 класа: Крестьянин, Лучник, Мечник(Танк) и Монах(маг).

   у каждого класса есть свои параметры здаровья, атаки и  защиты.
   
   Магии в игре нет, ответного удара таже нет, вообще тут мало что есть из оригинальной игры.
   
   В игре нет отдельного сущесва каждого класса, есть отряды(отряд может состоять только юнитов одного класса).
   
   Сила отряда зависит от кол-ва юнитов в нём.
   
   
   Инструкция к игре: 
   1. Создание юнитов:
        Для начала нужно выбрать класс: k(Крестьянин), l(Лучник), t(Мечник), m(Монах)
        Определение кол-ва юнитов в отряде осуществляется через метод spawn(n), где n это число(желательно целое)
        Пример: k.spawn(10) - мы создали 10 Крестьян
   2. Атака отряда:
        Для атаки отряда нужно выбрать отряд, который будет бить и которого будут бить. Всё это делается через метод attack()
        Пример: k.attack(l) - мы ударили Лучников(которых мы кстати ещё не создали)
   3. Баги просьба не искать!'''

'''Приятного времяпровождения!!!'''

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
            damage_after_damage = self.total_attack() - (self.base_attack * (health_after_damage // self.base_health))
            if health_after_damage > 0:
                print(f"{self.name} теряет {damage} здоровья. Осталось здоровья: {health_after_damage}. Текущий урон отряда: {damage_after_damage}")
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


l.spawn(15)
k.spawn(10)
k.attack(l)
l.attack(k)