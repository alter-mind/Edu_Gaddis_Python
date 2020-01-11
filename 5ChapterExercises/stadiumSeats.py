A = 20
B = 15
C = 10

def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    a = get_valid('Введите количество проданных мест класса A: ') * A
    b = get_valid('Введите колличество проданных мест класса B: ') * B
    c = get_valid('Введите колличество проданных мест класса С: ') * C
    print('Доход от продажи билетов составляет:', a + b + c)