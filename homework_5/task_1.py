from collections import namedtuple

def corp_revenues_nt():
    try:
        n_corp = int(input('Введите количество предприятий для расчета прибыли: '))
    except ValueError:
        print('Ошибка ввода.')
        return corp_revenues_nt()

    Company = namedtuple('Company', ['name', 'revenues'])
    companies = []
    revenues = 0
    for i in range(n_corp):
        name = input('Введите название предприятия: ').strip()
        revenue = input('Через пробел введите прибыль данного предприятия '
                        'за каждый квартал(Всего 4 квартала): ').split(' ')
        revenue = list(map(int, revenue))
        company = Company(name, revenue)
        companies.append(company)
        revenues+=sum(company.revenues)

    avg = revenues/n_corp
    print(f'Средняя годовая прибыль всех предприятий: {avg}')

    good, bad = [], []
    for comp in companies:
        good.append(comp.name) if sum(comp.revenues) > avg else bad.append(comp.name)

    print('Предприятия с прибылью выше среднего значения: ')
    for el in good:
        print(el)
    print('Предприятия с прибылью ниже среднего значения: ')
    for el in bad:
        print(el)

corp_revenues_nt()

