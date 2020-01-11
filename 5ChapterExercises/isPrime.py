import math
def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (целое, положительное) значение: '))
    return value

def calc():
    number = get_valid('Введите число для проверки на простоту: ')
    if (number == 1) or (number == 2) or (number == 3):
        print('это простое число')
    else:
        flag = False
        for i in range(2,int(math.sqrt(number)) + 1):
            if number % i == 0:
                print('Это составное число')
                flag = True
                break
        if not(flag):
            print('Это простое число')