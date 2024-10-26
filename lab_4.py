import random as r
class Planeta:

    def __init__(self, name, gungan_count, square):
        self.gungan_count = gungan_count
        self.name = name
        self.square = square

    @staticmethod
    def what_is_planeta(gungan_count):
        if gungan_count <= 2:
            planeta_is = 'Не имеет разумной жизни, вроде'
        elif gungan_count <= 10000000:
            planeta_is = 'Малонаселённая'
        elif gungan_count > 10000000:
            planeta_is = 'Крупнонаселённая'
        return planeta_is
    

    @classmethod
    def prirost_naseleniя(gungan_count):
        gungan_count += int(gungan_count)*0.4
        return gungan_count

    
    @property
    def ivent(gungan_count):
        if r.randint(1, 100) == 1:
            gungan_count -= gungan_count*0.8


    '''@gungan_count.setter
    def gungan_count(self):
        self.gungan_count = r.randint(0, 10000000000)'''



planeta = Planeta('Набу', r.randint(0, 10000000000), r.randint(800, 10000000))
print('Начальные данные планеты:')
print(f'Название планеты: {planeta.name}')
print(f'Площадь планеты: {planeta.square} км**2')
print(f'Планета: {planeta.what_is_planeta(planeta.gungan_count)}')
print(f'Население: {planeta.gungan_count}')
print(f'Плотность населения: {planeta.gungan_count/planeta.square}')

day = int(input())

for i in range(day):
    Planeta.prirost_naseleniя
    Planeta.prirost_naseleniя()
