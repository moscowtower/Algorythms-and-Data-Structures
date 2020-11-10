from collections import defaultdict
from functools import reduce as r

def hexcalc():
    dd = defaultdict(list)
    for i in range(2):
        inpt = input(f'Введите {i+1}е hex-число: ')
        dd[f'{i+1}-{inpt}'] = list(inpt)
    print(dd)

    soom = sum([int(''.join(i), 16) for i in dd.values()])
    print('Сумма = ', list('%X' % soom))

    result = r(lambda a, b: a *b, [int(''.join(i), 16) for i in dd.values()])
    print('Произведение = ', list('%X' % result))


hexcalc()