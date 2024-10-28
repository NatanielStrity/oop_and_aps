class Creature:
    """Базовый класс для всех существ."""
    
    def __init__(self, name, base_health, base_attack, base_defense):
        self.name = name                  # Имя существа
        self.base_health = base_health    # Базовое здоровье
        self.base_attack = base_attack     # Базовая атака
        self.base_defense = base_defense   # Базовая защита
        self.count = 1                    # Количество существ

    def set_count(self, count):
        """Устанавливаем количество существ."""
        self.count = count

    def total_attack(self):
        """Общая атака (изменяется в зависимости от количества)."""
        return self.base_attack * self.count

    def total_health(self):
        """Общее здоровье (изменяется в зависимости от количества)."""
        return self.base_health * self.count

    def total_defense(self):
        """Общая защита (остаётся постоянной)."""
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
            if health_after_damage > 0:
                print(f"{self.name} теряет {damage} здоровья. Осталось здоровья: {health_after_damage}.")
            else:
                print(f"{self.name} погибает.")
        else:
            print(f"Атака {self.name} не нанесла урона.")


class StrongWarrior:
    """Класс сильного воина с двумя типами атак."""

    def __init__(self, name):
        self.name = name                    # Имя воина
        self.base_health = 150              # Базовое здоровье
        self.base_attack = 30               # Базовая атака (тип 1)
        self.base_defense = 10              # Базовая защита
        self.count = 1                      # Количество существ

    def set_count(self, count):
        self.count = count

    def total_attack(self):
        """Общая атака (изменяется в зависимости от количества)."""
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def normal_attack(self, other):
        """Обычная атака."""
        print(f"{self.name} использует обычную атаку!")
        super().attack(other)

    def special_attack(self, other):
        """Специальная атака с высоким уроном."""
        damage = (self.total_attack() * 2) - other.total_defense()
        damage = max(damage, 0)
        
        print(f"{self.name} использует специальную атаку на {other.name}!")
        other.take_damage(damage)


class MagicBeast:
    """Класс магического существа."""

    def __init__(self, name):
        self.name = name
        self.base_health = 80
        self.base_attack = 25
        self.base_defense = 5
        self.count = 1

    def set_count(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name} использует магическую атаку!")
        super().attack(other)


class ForestGuardian:
    """Класс стража леса."""

    def __init__(self, name):
        self.name = name
        self.base_health = 120
        self.base_attack = 20
        self.base_defense = 15
        self.count = 1

    def set_count(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name} использует защитное заклинание!")
        super().attack(other)


class DarkKnight:
    """Класс Темного Рыцаря."""

    def __init__(self, name):
        self.name = name
        self.base_health = 100
        self.base_attack = 35
        self.base_defense = 10
        self.count = 1

    def set_count(self, count):
        self.count = count

    def total_attack(self):
        return self.base_attack * self.count

    def total_health(self):
        return self.base_health * self.count

    def total_defense(self):
        return self.base_defense

    def attack(self, other):
        print(f"{self.name} использует атаку Тьмы!")
        super().attack(other)
