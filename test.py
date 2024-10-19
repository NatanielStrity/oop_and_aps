class SpaceShip:
    def __init__(self, weight):
        self.weight = weight

    # геттер
    @property
    def weight(self):
        return self.weight

    # сеттер
    @weight.setter
    def weight(self, weight):
        if weight <= 100:
            self._weight = 100
        elif weight > 5000:
            self._weight = 5000
        else:
            self._weight = weight

            
def get_weight_info(self):
    print(f"Вес космического корабля составляет {self._weight} тонн.")


space_ship_1 = SpaceShip(90)
space_ship_1.get_weight_info()