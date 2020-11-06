"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return # Возвращает None даже если здесь указать return revers_num, яннп
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num): # Выигрышное решение, так как нет числовых и логических операций, только строковые
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

input = int(input('Введите число: '))

print(f'Рекурсивное решение: ', timeit(f'revers({input})', setup='from __main__ import revers', number=10000))
print(f'Цикличное решение: ', timeit(f'revers_2({input})', setup='from __main__ import revers_2', number=10000))
print(f'Строковое решение: ', timeit(f'revers_3({input})', setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')

