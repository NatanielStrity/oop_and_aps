class Puppy:
    states = ["Болеет", "Выздоравливает", "Здоров"]

    def __init__(self, index):
        self.index = index
        self.state = self.states[0]

    def get_treatment(self):
        current_state_index = self.states.index(self.state)
        if current_state_index < len(self.states) - 1:
            self.state = self.states[current_state_index + 1]
        else:
            print(f"Щенок {self.index} уже здоров.")

    def is_healthy(self):
        return self.state == self.states[-1]

class Dog:
    def __init__(self, puppies_count):
        self.puppies = [Puppy(i) for i in range(1, puppies_count + 1)]

    def heal_all(self):
        for puppy in self.puppies:
            puppy.get_treatment()

    def all_are_healthy(self):
        return all(puppy.is_healthy() for puppy in self.puppies)

    def give_away_all(self):
        self.puppies = []
        print("Все щенки были отданы в хорошие руки.")

class Vet:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def work(self):
        self.plant.heal_all()
        print(f"Ветеринар {self.name} ухаживает за собакой.")

    def care(self):
        if self.plant.all_are_healthy():
            print('всё гуд')
            self.plant.give_away_all()
        else:
            print("Не все щенки вылечились. Необходимо продолжить уход.")

    def knowledge_base(self):
        print("Информация по уходу за щенками:\n"
              "1. Обеспечьте щенкам полноценное питание.\n"
              "2. Регулярно проводите вакцинацию.\n"
              "3. Обеспечьте щенкам достаточную физическую активность.\n"
              "4. Следите за их поведением и обращайтесь к ветеринару при необходимости.")

# Тесты
vet_1 = Vet("Иван", Dog(3))
vet_1.knowledge_base()

print("\nУход за щенками:")
while not vet_1.plant.all_are_healthy():
    vet_1.work()
    vet_1.care()

vet_1.care()