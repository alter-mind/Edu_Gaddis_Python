def calc():
    try:
        file_name = 'steps.txt'
        file = open(file_name, 'r')
        for month in range(1,13): # вычисление среднего по месяцам
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                print('В ' + str(month) + ' в среднем сделано ' + str(count_average(31,file)) + ' шагов')
            elif month == 2:
                print('В ' + str(month) + ' в среднем сделано ' + str(count_average(28,file)) + ' шагов')
            else:
                print('В ' + str(month) + ' в среднем сделано ' + str(count_average(30,file)) + ' шагов')
    except IOError: # если steps.txt не существует, предложить сгенерировать со случайными данными
        print('Файл ' + file_name + ' не обнаружен на диске')
        if input('Хотите сгенерировать файл со случайными данными? [1/0]: ') == '1':
            file = open(file_name, 'w')
            for i in range(count):
                file.write(str(random.randrange(15001)) + '\n')
    except: # если всё-таки что-то пошло не так, пусть об этом будет известно
        print('Ошибка: что-то пошло не так')
    finally: # ну и закрыть файл в любом случае
        file.close()
# функция чтения шагов из файла за необходимое количество дней 
# вычисляет среднее количество шагов
def count_average(days,file):
    try:
        sum = 0
        for i in range(days):
            sum += int(file.readline())
        return int(sum / days)
    except: # Если при обработке файла произошла ошибка - предложить сгенерировать новый
        print('Файл ' + file_name + ' содержит некорректные или повреждённые данные')
        if input('Хотите сгенерировать файл со случайными данными? [1/0]: ') == '1':
            file = open(file_name, 'w')
            for i in range(count):
                file.write(str(random.randrange(15001)) + '\n')
