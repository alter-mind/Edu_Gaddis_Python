FAT = 9
CARB = 4

def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    fat = get_valid('Введите колличество жиров в граммах: ')
    carb = get_valid('Введите колличество углеводов в граммах: ')
    print('Калории из жиров:', str(format(fat * FAT, '.2f')))
    print('Калории из углеводов:', str(format(carb * CARB, '.2f')))

