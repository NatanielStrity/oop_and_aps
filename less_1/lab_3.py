class Puppy:
    states = ['Болеет', 'Выздоравливает', 'Здоров']


    def __init__(self, index):
        self.index = index
        self.state = self.states[0] #нач сост
    

    def get_treatment(self):
        current_state_index = self.states.index(self.state)
        if current_state_index < len(self.states) - 1: 
            self.state = self.states[current_state_index + 1] # если не ласт уровень, то +1 к состоянию
        else:
            print("Щенок уже здоров.")


    def is_healthy(self):
        return self.state == self.states[-1] #проверка всех щенят на положительное состояние


class Dog:
    def __init__(self, number_of_puppies):
        self.puppies = []
        for i in range(number_of_puppies):
            puppy = Puppy(i)            #создание щенка с индексом i
            self.puppies.append(puppy) #добавление ценка в список
            

    def heal_all(self):      #лечит всех на 1 ед. зоровья
        for index in range(len(self.puppies)):
            puppy = self.puppies[index]
            puppy.get_treatment()


    def all_are_healthy(self):  #проверяет все ли здоровы
        for puppy in self.puppies:
            if not puppy.is_healthy():
                return False
            return True


    def give_away_all(self):
        self.puppies.clear() #отчистка списка щенков
        print("Все щенки были отданы в хорошие руки.")


class Vet:
    def __init__(self, name):
        self.name = name
        self.plant = Dog(5)


    def work(self):     #уход за собакой
        while vet.plant.all_are_healthy == False:
            self.plant.heal_all()
            print("Ветеринар ухаживает за собакой.")


    def care(self):                   #пристройка щенят
        if self.plant.all_are_healthy():
            print('всё гуд')
            self.plant.give_away_all()
            
        else:
            print('Не все щенки вылечились. Необходимо продолжить уход.')


    def knowledge_base(self):
        print("Как ухаживать за щенками:")
        print("1. Обеспечьте щенкам сбалансированное питание.")
        print("2. Регулярно проводите вакцинацию.")
        print("3. Обеспечьте физическую активность и игры.")
        print("4. Проверьте здоровье щенков у ветеринара.")


if __name__ == "__main__":
    vet = Vet('Влад')

    vet.knowledge_base()

    vet.work()
    vet.care()
    print('Уход за щенками:')

