from random import randint

slovar = {'Компания ' + chr(65+i) : randint(10000, 1000000) for i in range(15)}

# 1
def find_max1(dikt):
    dikt_copy = dikt.copy()
    dikt_copy = {comp : rev for comp, rev in sorted(dikt_copy.items(), key=lambda revenue: revenue[1], reverse=True)[:3]} # O(n log n)
    for comp, rev in dikt_copy.items():  # O (n)
        print(f'{comp}, имеет годовую прибыль в ${rev}')

    # O(n log n) + O(n) = O(n)

# 2
def find_max2(dikt):
    dikt_copy = dikt.copy()
    for i in range(3):
        print(f'{max(dikt_copy, key=dikt_copy.get)} имеет годовую прибыль в ${dikt_copy.pop(max(dikt_copy, key=dikt_copy.get))}')

    # O(2 * max(dikt, dikt.get)) + O(1) = O(n)

# 3
def find_max3(dikt):
    comps, revs = [], []
    for comp, rev in dikt.items():
        comps.append(comp)  # O(1)
        revs.append(rev)    # O(1)
    revs.sort()             # O(n log n)
    revs = (revs[::-1])[:3]
    for comp, rev in dikt.items(): # O(n)
        if rev in revs:            # O(n)
            print(f'{comp} имеет годовую прибыль в ${rev}')

    # O(1) + O(1) + O(n log n) + (O(n) * O(n) = O(n^2) + O(n log n) + O(2) = O(n^2)

"""
Сложности по вариантам:
1. O(n)
2. O(n)
3. O(n^2)

Первые два варианта оказались эффективнее, потому что не используют вложенных циклов,
а в качестве сортировочных алгоритмов пользуются эффективными встроенными и анонимной функциями.
"""

find_max1(slovar)
print('--------------')
find_max2(slovar)
print('--------------')
find_max3(slovar)
