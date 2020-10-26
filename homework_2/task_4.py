def antiFib(n, a=1, elements=[]):
    if n == 0:
        result = sum(elements)
        print( f'Количество элементов {len(elements)}, их сумма - {result}')
        elements.clear() # без этого при последующем вызове функции добавление элементов продолжается с того же момента
        return
    elements.append(a)
    a = a * (-1 / 2)
    n -= 1
    antiFib(n, a)

a = antiFib(3)
b = antiFib(5)
c = antiFib(15)