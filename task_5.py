# Класс стека тарелок
class PlateStack():
    def __init__(self):
        self.stack = []
        # Максимум 5 тарелок в стопке
        self.capacity = 5

    def isEmpty(self):
        return self.stack == []

    def putPlate(self, plate):
        if self.capacity > 0:
            self.stack.append(plate)
            self.capacity-=1
        else:
            return None

    def getSize(self):
        return len(self.stack)

    def getCapacity(self):
        return self.capacity

    def lookAtTopPlate(self):
        print(self.stack[len(self.stack)-1])

    def takePlate(self):
        self.capacity+=1
        return self.stack.pop()

# Вычислительная функция
def fill_stacks(*args):
    result = []
    list_args = list(args)
    amount = len(list_args)
    for i in range(amount//5):
        ps = PlateStack()
        for k in range(5):
            ps.putPlate(list_args[k + i*5])
        result.append(ps)
    if amount % 5 != 0:
        nps = PlateStack()
        for j in range(amount % 5): #остаток
            nps.putPlate(list_args[amount + j - amount%5])
        result.append(nps)
    return result

# Вспомогательная функция
def beautify(list_of_stacks):
    print(f'Всего стеков: {len(list_of_stacks)}')
    a = 0
    b = 0
    for el in list_of_stacks:
        if el.getCapacity() == 0:
            a+=5
        else:
            b = el.getCapacity()
    print(f'Полных: {a}')
    if b:
        print(f'Незаполненный имеет {b} свободных мест')
        print(f'Стеки были собраны из {a + 5-b} тарелок')
    else:
        print(f'Стеки были собраны из {a + 5-b} тарелок')

res = fill_stacks(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
beautify(res)
print()
res2 = fill_stacks(1,'two', True, [1,2,3,4])
beautify(res2)
print()
res3 = fill_stacks(1,2,3,4,5)
beautify(res3)