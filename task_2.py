from random import randint
#
def find_min1(lst_obj):
    min = lst_obj[0] if lst_obj else None
    for i in lst_obj:
        if i < min:
            min = i
    print(min)

def find_min2(lst_obj):
    lst_obj.sort()
    print(lst_obj[0])


lst = [randint(0, 100) for x in range(10)]
find_min2(lst)
find_min2(lst)