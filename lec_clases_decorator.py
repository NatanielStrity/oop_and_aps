'''def decorator(cls):
	# Синтаксис декоратора класса

@decorator 
class A: 
  #Тело класса
  
#Другое объявленеие декоратора класса
def decorator(cls) : 
  	# Синтаксис декоратора класса
class B: 
  #Тело класса
 
B = decorator(B)  # Эквивалент в виде повторной привязки имени'''



def add_explosion(class_to_decorate):
    class DecoratedClass(class_to_decorate):
        def explode(self):
            print("Я взорвался!!!")

    return DecoratedClass

@add_explosion
class Planet:
    def exist(self):
        print("Я существую")

planet = Planet()
planet.exist()
planet.explode()