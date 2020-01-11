G = 9.8
def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    t = get_valid('Введите время падения в секундах: ')
    d = 0.5 * G * t**2
    print('Высота падения',d)