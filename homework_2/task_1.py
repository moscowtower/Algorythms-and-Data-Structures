def calculator():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    allowed = ['+', '-', '*', '/']
    if operation == '0':
        return None
    if operation in allowed:
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')
            a, b = None, None # Очищение значений, чтобы при развертывании функции обратно не ругалась консоль
        if a and b:
            if operation == '+':
                print(a+b)
            elif operation == '-':
                print(a-b)
            elif operation == '*':
                print(a*b)
            elif operation == '/':
                print(a/b)
    else:
        print('Ошибка ввода. Попробуйте еще раз')
    calculator()


calculator()