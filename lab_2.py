def decorator(func):
    def a(num1, num2, oper):
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
    return a

@decorator
def two_variables(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    
print(two_variables(6, 5, '+'))
    
    
            