def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    m = get_valid('Введите массу тела: ')
    v = get_valid('Введите скорость тела: ')
    energy = .5 * m * v**2
    print('Кинетическая энергия тела равна', energy)
