import random

def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (целое, положительное) значение: '))
    return value
def play():
    #print('Удадайте число от 0 до 100')
    number = random.randint(0, 101)
    if number == get_valid('Удадайте число от 0 до 100: '):
        print('Угадали')
    else:
        print('Не угадали, было загадоно число', number)
