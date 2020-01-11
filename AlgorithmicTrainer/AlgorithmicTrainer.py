selector = 1
def select():
    print('Алгоритмы на выбор: \n', 
          '1  Напишите цикл while с умножением предложенного пользователем числа на 100 пока результат не превышает 100\n',
          '2  Напишите цикл while, который складывает два предложенных пользователем числа и спрашивает желает ли пользователь продолжить итерации\n',
          '3  Напишите цикл for, который выводит приведённый ниже ряд чисел: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, ... , 100\n',
          '4  Напишите цикл, содержащий 10 итераций, который просит пользователя ввести число и вычисляет сумму нарастающего итога\n',
          '5  Напишите цикл, который вычисляет сумму числового ряда 1/30 + 2/29 + ... + 30/1\n',
          '6  Напишите серию вложенных циклов, которые выводя 10 строк по 15 символов #\n',
          '7  Напишите програмный код, который просит пользователя ввести положительное число и выполняет проверку введённого значения\n',
          '8  Напишите програмный код, который просит пользователя ввести цисло в диапазоне от 1 до 100 и выполняет проверку введённого значения.')
    selector = int(input('Выберите алгоритм для запуска, для выхода введитe 0:'))
    return selector
while selector != 0:
    selector = select()
    if selector == 1:
        print('Вы выбрали алгоритм 1')
        product = int(input('Введите положительное число: '))
        while product < 100:
            product *= 10
        print(product)
    elif selector == 2:
        print('Вы выбрали алгоритм 2')
        answer = 1
        while answer == 1:
            print('Введите два числа: ')
            a = int(input('Первое число: '))
            b = int(input('Второе число: '))
            print('Cумма', a + b)
            answer = int(input('Чтобы выполнить ещё раз введите 1, иначе 0: '))
    elif selector == 3:
        print('Вы выбрали алгоритм 3')
        for i in range(0,1001,10):
            print(i)
    elif selector == 4:
        print('Вы выбрали алгоритм 4')
        sum = 0
        for i in range(10):
            sum += float(input('Введите число: '))
            print('Сумма всех введённых чисел:',sum)
    elif selector == 5:
        print('Вы выбрали алгоритм 5')
        sum = 0
        for i in range(30):
            sum += (1+i)/(30-i)
        print('Сумма ряда:', format(sum, '.2f'))
    elif selector == 6:
        print('Вы выбрали алгоритм 6')
        for i in range(10):
            string = ''
            for j in range(15):
                string += '#'
            print(string)
    elif selector == 7:
        print('Вы выбрали алгоритм 7')
        number = float(input('Введите положительное число: '))
        while not(number > 0):
            number = float(input('Вы ввели неподходящее число. Введите положительное число: '))
    elif selector == 8:
        print('Вы выбрали алгоритм 8')
        number = float(input('Введите число в диапазоне от 1 до 100: '))
        while not(number in range(1,101)):
            number = float(input('Вы ввели неподходящее число. Введите число в диапазоне от 1 до 100: '))
    elif selector == 0:
        print('Выход из программы')
    else:
        print('Вы ввели неправильные данные')