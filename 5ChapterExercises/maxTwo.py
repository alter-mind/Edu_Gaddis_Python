def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (положительное) значение: '))
    return value
def calc():
    number1 = get_valid('Введите первое целое число: ')
    number2 = get_valid('Введите второе целое число: ')
    if number1 > number2:
        print('Большее из чисел:', number1)
    elif number2 > number1:
        print('Большее из чисел:', number2)
    else:
        print('Числа равны')
