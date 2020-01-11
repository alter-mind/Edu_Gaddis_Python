MILES = .6214

def convert():
    return get_valid() * MILES
def get_valid():
    kilometer = float(input('Введите расстояние в километрах: '))
    while not(kilometer > 0):
        kilometer = float(input('Введите корректное (положительное) значение в километрах: '))
    return kilometer
