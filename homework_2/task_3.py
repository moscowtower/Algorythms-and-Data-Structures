def myReverse(a, result=[]):
    if a == 0:
        result = ''.join(str(el) for el in result)
        print(f'Перевернутое число: {result}')
        return
    try:
        a = int(a)
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз.')
        return myReverse(input('Введите число, которое требуется перевернуть: '))
    num = a % 10
    a = a // 10
    result.insert(len(result), num)
    myReverse(a, result)

myReverse(input('Введите число, которое требуется перевернуть: '))