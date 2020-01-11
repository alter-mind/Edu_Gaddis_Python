import random
def print_all():
    try:
        file_name = input('Введите имя файла: ')
        file = open(file_name, 'r')
        string_number = 0
        for line in file:
            string_number += 1
            print(str(string_number) + ': ' + line.rstrip('\n'))
        file.close()
    except:
        print('Файл ' + file_name + ' не обнаружен.')
        try:
            numbers = int(input('Если вы хотите создать файл введите число записей\nДля выхода введите 0: '))
            if numbers > 0:
                file = open(file_name, 'w')
                for i in range(numbers):
                    file.write(str(random.randrange(100000000000000000000000000000000)) + '\n')
                file.close()
            elif numbers == 0:
                print('Выход из программы ')
            else:
                print('Не следовало вводить отрицательное число. Теперь программа вынуждена завершить работу :)')
        except ValueError:
            print('Ну просили же вас вводить ЧИСЛА. Теперь всё сломалось(')
