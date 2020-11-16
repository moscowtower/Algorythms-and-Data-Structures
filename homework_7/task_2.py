"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform

def mergesort(arr, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    mergesort(arr, left, middle)
    mergesort(arr, middle+1, right)
    merge(arr, left, right, middle)

def merge(arr, left, right, middle):
    lcopy = arr[left:middle+1]
    rcopy = arr[middle+1:right+1]

    lcopy_pointer = 0
    rcopy_pointer = 0
    sorted_pointer = left

    while lcopy_pointer < len(lcopy) and rcopy_pointer < len(rcopy):
        if lcopy[lcopy_pointer] <= rcopy[rcopy_pointer]:
            arr[sorted_pointer] = lcopy[lcopy_pointer]
            lcopy_pointer += 1
        else:
            arr[sorted_pointer] = rcopy[rcopy_pointer]
            rcopy_pointer += 1
        sorted_pointer += 1

    while lcopy_pointer < len(lcopy):
        arr[sorted_pointer] = lcopy[lcopy_pointer]
        lcopy_pointer += 1
        sorted_pointer += 1

    while rcopy_pointer < len(rcopy):
        arr[sorted_pointer] = rcopy[rcopy_pointer]
        rcopy_pointer += 1
        sorted_pointer += 1

if __name__ == '__main__':
    array_to_sort = [uniform(0, 50) for i in range(int(input('Введите количество элементов: ')))]
    print(f'Исходный массив: {array_to_sort}')
    mergesort(array_to_sort, 0, len(array_to_sort) - 1)
    print(f'Отсортированный массив: {array_to_sort}')

