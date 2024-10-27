class Unit_1:
    
    def __init__(self):
        self.hp = 10
        self.damage = 15
        self.protect = 5
    
    @classmethod
    def spawn(cls, count):
        all_hp = cls().hp * count
        all_damage = cls().damage * count
        return all_hp, all_damage, cls().hp, cls().damage

    def info():
        return print(f'Гоблин: {}')
    
goblin = Unit_1
goblin.spawn(10)
goblin.info()



    
