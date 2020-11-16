from random import randint
from timeit import timeit

array_to_sort = [randint(-100, 100) for i in range(100)]


def bubblesort(arr):
    a = arr
    n = 1
    while n < len(a):
        for el in range(len(a)-n):
            if a[el] < a[el+1]:
                a[el], a[el+1] = a[el+1], a[el]
        n += 1
    return a


def bubblesort_optimized(arr):
    a = arr
    n = 1
    while n < len(a):
        for el in range(len(a)-n):
            if a[el] < a[el+1]:
                a[el], a[el+1] = a[el+1], a[el]
            else:
                break
        n += 1
    return a

unopt = timeit('bubblesort(array_to_sort)', 'from __main__ import bubblesort, array_to_sort', number=10000)
opt = timeit('bubblesort_optimized(array_to_sort)', 'from __main__ import bubblesort_optimized, array_to_sort', number=10000)

print(f'Разница между временем выполнения обычной функции и оптимизированной составляет: {unopt-opt} секунд\n' 
      f'Что показывает, что оптимизированная функция быстрее в {unopt/opt} раз')

'''
Оптимизация обычным break'ом дала прирост эффективности в 11 раз, фантастика. Лишний перебор значений 
списка все еще дорого стоит.
'''