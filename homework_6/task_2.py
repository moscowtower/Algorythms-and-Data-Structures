from memory_profiler import profile

@profile
def f_str(*args):
    res = ''.join(str(args))
    return res

@profile
def concat_str(*args):
    res = ''
    for arg in args:
        res = res + str(arg)
    return res

if __name__ == '__main__':
    f_str([i for i in range(100000)])
    concat_str([i for i in range(100000)])

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     8     23.1 MiB     23.1 MiB           1   @profile
     9                                         def f_str(*args):
    10     23.2 MiB      0.2 MiB           1       res = ''.join(str(args))
    11     23.2 MiB      0.0 MiB           1       return res
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13     22.5 MiB     22.5 MiB           1   @profile
    14                                         def concat_str(*args):
    15     22.5 MiB      0.0 MiB           1       res = ''
    16     23.5 MiB      0.0 MiB           2       for arg in args:
    17     23.5 MiB      1.0 MiB           1           res = res + str(arg)
    18     23.5 MiB      0.0 MiB           1       return res

Форматирование строки вместо конкатенации дает выигрыш за счет того, что не выделяется память под временные строки
во время конкатенации, как это показано в цикле функции concat_str
'''