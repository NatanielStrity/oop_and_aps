def two_variables(num1, num2, oper):
    def decorator(func):
        def wrapper():
            if oper == '+':
                return func(num1, num2, oper)
            elif oper == '-':
                return func(num1, num2, oper)
            elif oper == '*':
                return func(num1, num2, oper)
            elif oper == '/':
                if num2 != 0 :
                    return func(num1, num2, oper)
                else:
                    print('НЕТ!!! ТАК НЕЛЬЗЯ!!!')
        return wrapper
    return decorator

@two_variables(6, 5, '+')
def culc(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    
print(culc())
    
    
            