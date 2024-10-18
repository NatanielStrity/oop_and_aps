def decorator(func):
    return func

@decorator
def decorate_example():
    print('Привет Вселенная!')
    
decorate_example()

# Другое объявление декоратора
decorate_example = decorator(decorate_example)
decorate_example()
