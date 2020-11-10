from collections import OrderedDict
from timeit import timeit

keys = [i for i in range(1500)]
values = [i for i in range(1500)]
uDict = dict(zip(keys, values))
oDict = OrderedDict(zip(keys, values))

print('Удаление последнего добавленного элемента: ')
print('Dict: ', timeit(f'uDict.popitem()', setup='from __main__ import uDict', number=500))
print('OrderedDict: ', timeit(f'oDict.popitem(last=True)', setup='from __main__ import oDict', number=500))

print('Удаление первого добавленного элемента: ')
print('Dict: функционал не поддерживается')
print('OrderedDict: ', timeit(f'oDict.popitem(last=True)', setup='from __main__ import oDict', number=500))

print('Добавление ключа в начало: ')
print('Dict: функционал не поддерживается')
print('OrderedDict: ', timeit(f'oDict.move_to_end(0, last=False)', setup='from __main__ import oDict', number=300))

'''
OrderedDict пока для меня самый странный персонаж, он вроде и хуже оптимизирован чем list или dict, но зато помнит
порядок, что иногда может быть важным. Родственник LinkedList'а из java
'''