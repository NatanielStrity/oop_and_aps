# Типо Заголовок(Тут должен был быть заголовок или ваша реклама, но её нет из-за меня и из-за Вас)

Это мини-игра была сделана на основе серии игр Heroes of Might and Magic
    
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
   3. Баги просьба не искать!

Приятного времяпровождения!!!