import math

def get_valid(message):
    value = int(input(message))
    while not(value > 0):
        value = int(input('Введите корректное (целое, положительное) значение: '))
    return value

def is_prime(number):
    if (number == 1) or (number == 2):
        return True
    else:
        flag = False
        for i in range(2,int(math.sqrt(number)) + 1):
            if number % i == 0:
                flag = True
                break
        if flag:
            return False
        else:
            return True

def get_number():
    return get_valid('Введите предел списка простых чисел: ')

def print_all():
    number = get_number()
    for i in range(1,number +1):
        if is_prime(i):
            print(i)