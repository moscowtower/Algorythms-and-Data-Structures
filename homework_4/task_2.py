import timeit

def memoize(func):
    # Рекурсивыные функции страдают при выполнении одних и тех же операций с одним и тем же результатом
    # Поэтому мы запишем результаты уже выполненных операций в словарь, чтобы обращаться к ним
    # Так как обращение к элементу словаря стоит дешевле некуда - O(1)
    memo = {}
    def inner(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return inner

@memoize
def recursive_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

rr = timeit.Timer('recursive_reverse(123456789)', 'from __main__ import recursive_reverse')
rr_result = rr.timeit(number=1000)
print(f'Без мемоизации: {rr_result}с')

rr_memo = timeit.Timer('recursive_reverse_memo(123456789)', 'from __main__ import recursive_reverse_memo')
rr_memo_result = rr_memo.timeit(number=1000)
print(f'С мемоизацией: {rr_memo_result}с')

print(f'Разница времени выполнения = {rr_result - rr_memo_result}с')
print(f'Функция с мемоизацией быстрее в {rr_result/rr_memo_result} раз')