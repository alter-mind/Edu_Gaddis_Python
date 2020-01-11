import random
def write_all():
    try:
        file_name = input('Введите имя файла: ')
        file = open(file_name, 'w')
        count = get_valid('Введите число случайных чисел для записи в файл: ')
        for i in range(count):
            file.write(str(random.randrange(501)) + '\n')
        file.close()
    except:
        print('Что-то пошло не так')
        file.close

def get_valid(message):
    try:
        value = int(input(message))
        while value <= 0:
            print('Вы ввели некорректное значение')
            value = int(input(message))
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)
