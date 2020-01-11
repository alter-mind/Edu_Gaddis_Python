ASSESSMENT = .6
TAX = 1 / 100 * .72
def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value
def calc():
    cost = get_valid('Введите фактическую стоимость недвижимости: ')
    print('Оценочная стоимость составляет:', str(cost * ASSESSMENT))
    print('Налог на недвижимость составляет:', str(cost * ASSESSMENT * TAX))

