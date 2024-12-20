class Unit:
    def __init__(self, name, health, defense, attack):
        self.name = name
        self.max_health = health
        self.health = health
        self.defense = defense
        self.attack = attack
        self.count = 0  # Количество юнитов в отряде

    def spawn(self, count):
        self.count += count  # Увеличиваем количество юнитов
        self.health = self.max_health  # Обновляем здоровье каждого нового юнита

    def total_health(self):
        return self.health * self.count

    def total_attack(self):
        return self.attack * self.count

    def is_alive(self):
        return self.health > 0

    def attack_unit(self, other):
        damage = self.total_attack() - other.defense
        if damage > 0:
            other.health -= damage
            if other.health < 0:
                other.health = 0
        print(f"{self.name} атакует {other.name}. Нанесено урона: {damage}. Оставшееся здоровье {other.name}: {other.health}")

    def __str__(self):
        return f"{self.name} (Количество: {self.count}, Здоровье: {self.health}, Урон: {self.attack})"
    


class Peasant(Unit):
    def __init__(self):
        super().__init__("Peasant", 30, 5, 10)
    
    def info(self):
        return print(f'{self.name}: Здоровье: {self.health}; Защита: {self.defense}; Атака: {self.attack}')


class Archer(Unit):
    def __init__(self):
        super().__init__("Archer", 20, 3, 15)

    def info(self):
        return print(f'{self.name}: Здоровье: {self.health}; Защита: {self.defense}; Атака: {self.attack}')



class Hero:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana
        self.units = {}  # Словарь для хранения юнитов

    def spawn(self, unit_class, count):
        unit_name = unit_class.__name__.lower()  # Получаем имя класса в нижнем регистре
        if unit_name not in self.units:
            self.units[unit_name] = unit_class()  # Создаем экземпляр юнита
        self.units[unit_name].spawn(count)  # Вызываем метод spawn юнита

    def attack(self, unit_name, enemy_hero, enemy_unit_name):
        # Получаем атакующего юнита
        attacking_unit = self.units.get(unit_name.lower())
        # Получаем защищающийся юнит противника
        defending_unit = enemy_hero.units.get(enemy_unit_name.lower())
        
        if attacking_unit is None:
            print(f"{self.name} не имеет юнита {unit_name}!")
            return
        if defending_unit is None:
            print(f"{enemy_hero.name} не имеет юнита {enemy_unit_name}!")
            return
        if not attacking_unit.is_alive():
            print(f"{attacking_unit.name} мёртв и не может атаковать.")
            return
        if not defending_unit.is_alive():
            print(f"{defending_unit.name} мёртв и не может быть атакован.")
            return

        attacking_unit.attack_unit(defending_unit)  # Производим атаку

    def info(self):
        return print(f"Герой: {self.name}, Мана: {self.mana}, Юниты: {[str(unit) for unit in self.units.values()]}")


if __name__ == "__main__":
    hero1 = Hero("Hero1", 100)
    hero2 = Hero("Hero2", 100)
    peasant = Peasant()
    archer = Archer()
    
    '''Пример создания отрядов в команде Героя'''
    hero1.spawn(Peasant, 5)
    hero1.spawn(Archer, 3)

    hero2.spawn(Peasant, 2)
    hero2.spawn(Archer, 4)

    '''Инфа о герое и его отрядах'''
    hero1.info()

    '''Пример атаки: Archer из команды hero1 атакает Peasant из команды hero2 '''
    hero1.attack("Archer", hero2, "Peasant") 
    hero2.attack("Archer", hero1, "Peasant") 

    '''Общая инфа о юните'''
    peasant.info()

    