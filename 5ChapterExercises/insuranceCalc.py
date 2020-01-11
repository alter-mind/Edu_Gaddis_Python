MIN = .8
cost = 0

def get_valid_cost():
    cost = float(input('Введите стоимость недвижимости: '))
    while not(cost > 0):
        cost = float(input('Введите корректную (положительную) стоимость недвижимости: '))
    return cost

def get_data():
    cost = get_valid_cost()

def recomended():
    return cost * MIN 

def print_all():
    print('Рекоммендованая минимальная сумма страховки составляет: ' + str(format(recomended(), ',.2f')))
