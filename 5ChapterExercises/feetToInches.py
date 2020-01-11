def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    feet = get_valid('Введите футы: ')
    inches = feet * 12
    print('В дюймах: ', inches)


