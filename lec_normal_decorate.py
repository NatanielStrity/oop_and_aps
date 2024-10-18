def decorator(func):
    def new_func():
        print('Казнить нельзя, помиловать!')
    return new_func

@decorator
def decorate_example():
    print('Казнить, нельзя помиловать.')

decorate_example()
