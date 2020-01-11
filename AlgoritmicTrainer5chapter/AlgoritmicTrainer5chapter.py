import random

def function_selector():
    number = int(input('Выберите алгоритм: '))
    if not(number in range(8)):
        number = int(input('Введённые данные не корректны. Выберите алгоритм: '))
    return number

def show_menu():
    print('Функции: \n1\tten_args\n2\tmyfunction\n3\trand 1-100\n4\thalf\n5\tcube\n6\ttimes_ten_return\n7\tget_first_name')

def times_ten(arg):
    print(str(arg * 10))

def my_function(a,b,c):
    d = (a + c) / b
    print(d)

def rand_1_100():
    return random.randrange(1,100)

def half(arg):
    return arg / 2

def cube(arg):
    return arg ** 3

def times_ten_return(arg):
    return arg * 10

def get_first_name():
    return input('Введите ваше имя: ')

def main():
    show_menu()
    select = function_selector()
    while select != 0:
        if select == 1:
            times_ten(float(input('Введите аргумент для функции times_ten: ')))
        elif select == 2:
            my_function(float(input('Введите аргумент "а" для функции my_function: ')), float(input('Введите аргумент "b" для функции my_function: ')), float(input('Введите аргумент "c" для функции my_function: ')))
        elif select == 3:
            print('функция rand_1_100 возвращает значение:',rand_1_100())
        elif select == 4:
            print('Результат работы функции half: ' + str(half(float(input('Введите аргумент для фунции half: ')))))
        elif select == 5:
            print('Результат работы фунции cube: ' + str(cube(float(input('Введите аргумент для функции cube: ')))))
        elif select == 6:
            print('Результат работы функции times_ten_return: ' + str(times_ten_return(float(input('Введите аргумент для функции times_ten_return: ')))))
        elif select == 7:
            print('Результат работы функции get_first_name: ' + str(get_first_name()))
        select = function_selector()
    print('Выполнен выход из программы')
main()