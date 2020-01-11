import random

def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (положительное) значение: '))
    return value

def start_test():
    number1 = random.randrange(100,1000)
    number2 = random.randrange(100,1000)
    sum = number1 + number2
    if sum == get_valid('Вычислите ' + str(number1) + '+' + str(number2) + '='):
        print('Очень хорошо')
    else:
        print('Вы не правы')
        print('Верный ответ: ' + str(sum))
