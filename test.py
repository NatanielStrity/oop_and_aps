class Unit:
    def __init__(self, name, health, defense, attack):
        self.name = name
        self.max_health = health
        self.health = health
        self.defense = defense
        self.attack = attack
        self.count = 0  # Количество юнитов

    def spawn(self, count):
        self.count += count
        self.health = self.max_health  # Сбрасываем здоровье после спавна

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


class Hero:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana
        self.units = {}

    def spawn(self, unit_class, count):
        unit = unit_class()  # Создаем экземпляр юнита
        unit.spawn(count)
        self.units[unit.name.lower()] = unit
        print(f"{self.name} создал {count} {unit.name}(ов).")

    def cast_stone_skin(self, unit_name):
        if unit_name.lower() not in self.units:
            print(f"{self.name} не имеет юнита {unit_name} в своей команде.")
            return
        
        unit = self.units[unit_name.lower()]  # Находим юнит по имени
        if self.mana >= 10:
            unit.defense += 12
            self.mana -= 10
            print(f"{self.name} использует каменную кожу на {unit.name}. Защита увеличена на 12.")
        else:
            print(f"{self.name} недостаточно маны для использования каменной кожи.")

    def attack(self, attacker_name, hero_target, target_name):
        if attacker_name.lower() not in self.units:
            print(f"{self.name} не имеет юнита {attacker_name} для атаки.")
            return
        
        attacker = self.units[attacker_name.lower()]  # Находим атакующего юнита
        if target_name.lower() not in hero_target.units:
            print(f"{hero_target.name} не имеет юнита {target_name} на которого можно атаковать.")
            return
        
        target = hero_target.units[target_name.lower()]  # Находим защищающегося юнита
        attacker.attack_unit(target)


# Пример использования:

class Peasant(Unit):
    def __init__(self):
        super().__init__("Peasant", 30, 2, 5)

class Archer(Unit):
    def __init__(self):
        super().__init__("Archer", 25, 1, 7)


if __name__ == "__main__":
    hero1 = Hero("Hero1", 100)
    hero2 = Hero("Hero2", 50)
    
    # Спавним юнитов
    hero1.spawn(Peasant, 5)
    hero2.spawn(Archer, 3)
    
    # Применяем заклинание
    hero1.cast_stone_skin("Peasant")
    
    # Атакуем
    hero1.attack("Peasant", hero2, "Archer")
