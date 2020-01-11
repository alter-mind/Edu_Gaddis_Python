def get_valid(message): #получение корректного числового значения
    try:
        value = int(input(message))
        if value <= 0:
            print('Номер счёта должен быть положительным числом')
            value = get_valid(message)
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)
def check_number():
    try:
        file = open('charge_account.txt','r') #открытие файла 
        number = get_valid('Введите номер счёта для проверки: ')
        numbers = []
        for line in file:
            numbers.append(int(line))
        if number in numbers:
            print('Допустимый номер счёта')
        else:
            print('Недопустимый номер счёта')

    except (IOError, ValueError): #Ошибка файла. Предложить сгенерировать файл со случайными данными
        print('Файл отсутствует на диске или содержит неправильные данные')
        answer = input('Сгенерировать новый файл со случайными данными? 1 - да, всё остальное - нет: ')
        if answer == '1':
            import random
            file = open('charge_account.txt', 'w')
            for i in range(1001):
                file.write(str(random.randrange(1000000,10000000)) + '\n')
            print('Файл создан')
        else:
            print('Для выхода из программы нажмите Enter')
            input()
    except Exception as e:
        print('Что-то пошло не так')
        print(e)
    finally:
        file.close()

