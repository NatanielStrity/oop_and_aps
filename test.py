class Goblin:
    def __init__(self):
        self.health = 10
        self.attack = 5
        self.defense = 2

    @classmethod
    def spawn(cls, quantity):
        total_health = cls().health * quantity
        total_attack = cls().attack * quantity
        return print({
            'type': 'Goblin',
            'quantity': quantity,
            'total_health': total_health,
            'total_attack': total_attack,
            'defense': cls().defense  # Защита постоянная
        })


class Orc:
    def __init__(self):
        self.health = 15
        self.attack = 7
        self.defense = 4

    @classmethod
    def spawn(cls, quantity):
        total_health = cls().health * quantity
        total_attack = cls().attack * quantity
        return {
            'type': 'Orc',
            'quantity': quantity,
            'total_health': total_health,
            'total_attack': total_attack,
            'defense': cls().defense  # Защита постоянная
        }


class Elf:
    def __init__(self):
        self.health = 12
        self.attack = 8
        self.defense = 3

    @classmethod
    def spawn(cls, quantity):
        total_health = cls().health * quantity
        total_attack = cls().attack * quantity
        return {
            'type': 'Elf',
            'quantity': quantity,
            'total_health': total_health,
            'total_attack': total_attack,
            'defense': cls().defense  # Защита постоянная
        }


class Dragon:
    def __init__(self):
        self.health = 50
        self.attack = 15
        self.defense = 10

    @classmethod
    def spawn(cls, quantity):
        total_health = cls().health * quantity
        total_attack = cls().attack * quantity
        return {
            'type': 'Dragon',
            'quantity': quantity,
            'total_health': total_health,
            'total_attack': total_attack,
            'defense': cls().defense  # Защита постоянная
        }

goblin = Goblin
goblin.spawn(4)