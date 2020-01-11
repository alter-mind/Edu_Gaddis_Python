def gender_check(): # Получение пола 
    try:
        gender = input('Для проверки имени мальчика введите 1, остальное - для проверки имени девочки: ')
        if gender == '1':
            return True # Мальчик
        else:
            return False # Девочка
    except:
        print('Выбор пола завершился с ошибкой')

def search(): # Поиск имени по спискам
    boy_file = 'BoyNamex.txt'
    girl_file = 'GirlNames.txt'
    if gender_check():
        name = input('Введите имя мальчика латиницей: ')
        name_check(boy_file, name)
    else:
        name = input('Введите имя девочки латиницей: ')
        name_check(girl_file, name)

def name_check(file_name,name): # Проверка имени на наличие в списке
    try:
        file = open(file_name, 'r')
        name_list = []
        for line in file:
            name_list.append(line.rstrip())
        if name in name_list:
            print('Имя найдено в списке')
        else:
            print('Имя не найдено в списке')
        file.close
    except IOError: # если файл не найден, сгенерировать со случайными данными для примера
        print('Файл с именами не найден на диске, будет сгенерирован файл с 200 случайными именами')
        gen_list_name(file_name)
        name_check(file_name,name)

def gen_name(): # Генерерование случайного имени
    import random
    name = ''
    name += chr(random.randrange(65,91))
    for i in range(random.randrange(2,9)):
        name += chr(random.randrange(97,123))
    return name

def gen_list_name(file_name): # Генерирование файла со случайными именами
    list_name = []
    while len(list_name) < 200:
        name = gen_name()
        if name not in list_name:
            list_name.append(name)
    file = open(file_name, 'w')
    for name in list_name:
        file.write(name + '\n')
    file.close


