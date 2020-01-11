import random
def print_all():
    try:
        file = open('numbers.txt', 'r')
        for line in file:
            print(line.rstrip('\n'))
        file.close()
    except:
        print('Файл "numbers.txt" не обнаружен.')
        try:
            numbers = int(input('Если вы хотите создать файл введите число записей\nДля выхода введите 0:'))
            if numbers > 0:
                file = open('numbers.txt', 'w')
                for i in range(numbers):
                    file.write(str(random.randrange(1000000000000000)) + '\n')
                file.close()
            elif numbers == 0:
                print('Выход из программы ')
            else:
                print('Не следовало вводить отрицательное число. Теперь программа вынуждена завершить работу :)')
        except ValueError:
            print('Ну просили же вас вводить ЧИСЛА. Теперь всё сломалось(')
