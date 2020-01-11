import random
def print_all():
    try:
        file_name = 'numbers.txt'
        file = open(file_name, 'r')
        sum = 0
        for line in file:
            sum += int(line)
        print('Сумма всех значений, хранящихся в файле равна', sum)
        file.close()
    except:
        print('Файл ' + file_name + ' не обнаружен или содержит неправильные данные')
        try:
            numbers = int(input('Если вы хотите создать файл введите число записей\nДля выхода введите 0: '))
            if numbers > 0:
                file = open(file_name, 'w')
                for i in range(numbers):
                    file.write(str(random.randrange(1000000000)) + '\n')
                file.close()
            elif numbers == 0:
                print('Выход из программы ')
            else:
                print('Не следовало вводить отрицательное число. Теперь программа вынуждена завершить работу :)')
        except ValueError:
            print('Ну просили же вас вводить ЧИСЛА. Теперь всё сломалось(')

