file_name = 'GolfPoints.txt'

def write_all():
    try:
        file = open(file_name, 'w')
        flag = True
        while flag:
            file.write(input('Введите имя игрока: ') + '\n')
            file.write(str(get_valid('Введите количество очков: ')) + '\n')
            if get_valid('желаете добавить ещё одного игрока? [1/0]: ') == 1:
                flag = True
            else:
                flag = False
        file.close()
    except:
        print('Что-то пошло не так')
        file.close()

def read_all():
    try:
        file = open(file_name, 'r')
        name = file.readline().rstrip('\n')
        while name != '':
            print(name + '\t' + file.readline().rstrip('\n'))
            name = file.readline().rstrip('\n')
    
    except IOError:
        print('Похоже файла с данными игроков ещё не существует')
        if get_valid('Создать файл? [1/0]: ') == 1:
            write_all()
    except:
        print('Что-то пошло не так или я накосячил пытаясь сократить код')

def get_valid(message):
    try:
        value = int(input(message))
        while value < 0:
            print('Вы ввели некорректное значение')
            value = int(input(message))
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)
