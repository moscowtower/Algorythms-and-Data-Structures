"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit

def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def eratosthenes(n):
    top_border = 10000
    a = [i for i in range(top_border)]
    a[1] = 0
    i = 2
    while i < top_border:
        if a[i] != 0:
            j = i * 2
            while j < top_border:
                a[j] = 0
                j += i
        i += 1
    a = set(a)
    a.remove(0)
    return sorted(list(a))[n-1]

s10 = timeit('simple(10)', 'from __main__ import simple', number=100)
s100 = timeit('simple(100)', 'from __main__ import simple', number=100)
s1000 = timeit('simple(1000)', 'from __main__ import simple', number=100)
e10 = timeit('eratosthenes(10)', 'from __main__ import eratosthenes', number=100)
e100 = timeit('eratosthenes(100)', 'from __main__ import eratosthenes', number=100)
e1000 = timeit('eratosthenes(1000)', 'from __main__ import eratosthenes', number=100)

print(f'Результаты для simple (10, 100, 1000): {s10} сек., {s100} сек., {s1000} сек.')
print(f'Результаты для eratosthenes (10, 100, 1000): {e10} сек., {e100} сек., {e1000} сек.')

"""
Функция без решета была быстрее для чисел с порядковым номером <1000, 
однако в случаях с >1000 бедная simple() просто захлебнулась

simple() = O (n^2)
eratosthenes = O log n, либо O log (log n)
"""