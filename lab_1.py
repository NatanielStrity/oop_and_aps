def decorator(number):
    def summator(func):
         def wrapper(*args, **kwargs):
            a = func(*args, **kwargs) + number
            return print(a)
         return wrapper
    return summator
    

@decorator(4)
def get_number():
    return 10

result = get_number()
