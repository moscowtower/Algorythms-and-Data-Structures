from collections import deque
from timeit import timeit
temp = [1, 2, 55, 123, 11, 2, 912]

myList = list(temp)
myDeque = deque(temp)

print('Добавление нового элемента в конец:')
print('List: ', timeit(f'myList.append(25)', setup='from __main__ import myList', number=1000))
print('Deque: ', timeit(f'myDeque.append(25)', setup='from __main__ import myDeque', number=1000))
print('------------------------------')
print('Добавление нового элемента в начало:')
print('List: ', timeit(f'myList.insert(1, 50)', setup='from __main__ import myList', number=1000))
print('Deque: ', timeit(f'myDeque.appendleft(50)', setup='from __main__ import myDeque', number=1000))
print('------------------------------')
print('"Вытаскивание" элемента с начала:')
print('List: ', timeit(f'myList.pop(0)', setup='from __main__ import myList', number=1000))
print('Deque: ', timeit(f'myDeque.popleft()', setup='from __main__ import myDeque', number=1000))
print('------------------------------')
print('"Вытаскивание" элемента с конца:')
print('List: ', timeit(f'myList.pop()', setup='from __main__ import myList', number=1000))
print('Deque: ', timeit(f'myDeque.pop()', setup='from __main__ import myDeque', number=1000))
print('------------------------------')
print('Удаление конкретного элемента:')
print('List: ', timeit(f'myList.remove(123)', setup='from __main__ import myList', number=1))
print('Deque: ', timeit(f'myDeque.remove(123)', setup='from __main__ import myDeque', number=1))

"""
Deque сильно выигрывает по всем запросам, кроме удаления конкретного элемента, как скорее всего и "выдачи" конкретного
элемента. К счастью, документация Python нас не обманывает.
"""