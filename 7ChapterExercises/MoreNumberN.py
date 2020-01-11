def get_valid(message): #получение корректного числового значения
    try:
        value = float(input(message))
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)

def get_n(): #получить число n
    try: 
        n = get_valid('Введите число n: ')
        return n
    except:
        print('Нужно вводить число')
        get_n()

def get_list(): #получить число элементов списка и заполнить список случайными числами в диапазоне 1-99
    try:
        import random
        items = int(get_valid('Введите количество элементов списка: '))
        numbers_list = []
        for i in range(items):
            numbers_list.append(random.randrange(1,100))
        return numbers_list
    except:
        print('Колличество элементов списка - целое положительное число')
        get_list()

def compare_and_print(n, numbers_list): #сравнение значений списка с n и вывод тех, которые больше
    try:
        for number in numbers_list:
            if number > n:
                print(number)
    except:
        print('Во время работы сравнения числа со списком проихошла ошибка. Возможно были получены неправильные данные')
    
