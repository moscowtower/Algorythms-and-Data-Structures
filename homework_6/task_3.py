from memory_profiler import profile

@profile
def recursive_fib(n):
    if n <= 0:
        print("Ошибка ввода")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)

if __name__ == '__main__':
    # recursive_fib(10000) == maxim recursion depth bla bla bla
    recursive_fib(10)

"""
Подводный камень в самой рекурсии - профилировка будет выполняться для каждого прохода функции, что не позволит 
произвести профилировку с высокой нагрузкой
"""