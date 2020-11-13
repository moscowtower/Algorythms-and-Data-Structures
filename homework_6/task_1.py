from memory_profiler import profile

@profile
def fib(n):
    if n <= 0:
        print("Ошибка ввода")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))

@profile
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

print(reverseArray([59, 23, 11, 23, 22, 5543, 1], 0, 6))

@profile
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum

print(sumOfSeries(10))
"""
Windows x64
Python 3.8.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fib():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     18.7 MiB     18.7 MiB           9   @profile
    19                                         def fib(n):
    20     18.7 MiB      0.0 MiB           9       if n <= 0:
    21                                                 print("Ошибка ввода")
    22     18.7 MiB      0.0 MiB           9       elif n == 1:
    23     18.7 MiB      0.0 MiB           2           return 0
    24     18.7 MiB      0.0 MiB           7       elif n == 2:
    25     18.7 MiB      0.0 MiB           3           return 1
    26                                             else:
    27     18.7 MiB      0.0 MiB           4           return fib(n-1)+fib(n-2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
reverseArray():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     18.7 MiB     18.7 MiB           1   @profile
    32                                         def reverseArray(arr, start, end):
    33     18.7 MiB      0.0 MiB           4       while (start < end):
    34     18.7 MiB      0.0 MiB           3           temp = arr[start]
    35     18.7 MiB      0.0 MiB           3           arr[start] = arr[end]
    36     18.7 MiB      0.0 MiB           3           arr[end] = temp
    37     18.7 MiB      0.0 MiB           3           start += 1
    38     18.7 MiB      0.0 MiB           3           a = list(arr)
    39     18.7 MiB      0.0 MiB           3           end = end-1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sumOfSeries():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     18.7 MiB     18.7 MiB           1   @profile
    41                                         def sumOfSeries(n):
    42     18.7 MiB      0.0 MiB           1       sum = 0
    43     18.7 MiB      0.0 MiB          11       for i in range(1, n + 1):
    44     18.7 MiB      0.0 MiB          10           sum += i * i * i
    45     18.7 MiB      0.0 MiB           1       return sum


На мой взгляд профайлер либо не работает на моей машине, либо его что-то глушит, либо же расход памяти настолько мизерный,
что он не в состоянии его посчитать????
"""