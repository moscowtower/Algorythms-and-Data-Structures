import time

def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - begin} секунд')

    return inner

@calculate_time
def fill_list():
    list = []
    for i in range(100000):
        list.insert(0, i)
    return list

@calculate_time
def fill_dict():
    dikt = {}
    for i in range(100000):
        dikt[i]=f'{i}'
    return dikt

fill_dict()
fill_list()