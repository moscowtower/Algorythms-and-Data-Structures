import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_nums = [i for i, j in enumerate(nums) if j % 2 == 0] # Enumerate дарит кортеж, который быстрее списка
    return new_nums

f1_timer = timeit.Timer('func_1([i for i in range(100)])', 'from __main__ import func_1')
f2_timer = timeit.Timer('func_2([i for i in range(100)])', 'from __main__ import func_2')
print(f1_timer.timeit(number=10000))
print(f2_timer.timeit(number=10000))