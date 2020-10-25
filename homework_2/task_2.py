def evenOrNot(a, even=0, odd=0):
    if a == 0:
        print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')
        return
    num = a % 10
    if num % 2 == 0:
        even+=1
    else:
        odd+=1
    a = a // 10
    evenOrNot(a, even, odd)

a = int(input('Введите число: '))
evenOrNot(a)
