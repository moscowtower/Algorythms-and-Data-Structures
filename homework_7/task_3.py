from random import randint, choice
from statistics import median

# Спасибо Тони Хоару за квикселект и его применимость к несортированным массивам,
# а также гикбреинс за бессонные ночи за питоном <33

m = int(input('Введите m: '))
array = [randint(-100, 100) for _ in range(2 * m + 1)]

def quickselect_median(array, pivot_fn=choice):
    if len(array) % 2 == 1:
        return quickselect(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(array, len(array) / 2 - 1, pivot_fn) +
                      quickselect(array, len(array) / 2, pivot_fn))


def quickselect(array, index, pivot_fn):
    if len(array) == 1:
        # assert выглядит более адекватной версией того, что я делал с помощью UserWarning
        assert index == 0
        return array[0]

    pivot = pivot_fn(array)

    lows = [i for i in array if i < pivot]
    highs = [i for i in array if i > pivot]
    pivots = [i for i in array if i == pivot]

    if index < len(lows):
        return quickselect(lows, index, pivot_fn)
    elif index < len(lows) + len(pivots):
        # При великой удачи:
        return pivots[0]
    else:
        return quickselect(highs, index - len(lows) - len(pivots), pivot_fn)

print('Медианы совпадают') if quickselect_median(array) == median(array) else print('Медианы НЕ совпадают')

"""В отработку предыдущего задания, где я привел мало примеров - привожу реализации шелла и гномьей сортировок"""

def shellsort(array):
    def new_increment(array):
        i = len(array) // 2
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i/2.2))
            yield i
    for inc in new_increment(array):
        for i in range(inc, len(array)):
            for j in range(i, inc - 1, -inc):
                if array[j - inc] < array[j]:
                    break
                array[j], array[j - inc] = array[j - inc], array[j]
                return array

def shellsort2(array):
    n = len(array)
    gap = n / 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap /= 2

def gnomesort( arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
