def get_valid(message): #получение корректного числового значения
    try:
        value = float(input(message))
        while value < 0:
            print('Вы ввели некорректное значение')
            value = int(input(message))
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)

def get_rainfall_per_month():
    try:
        rainfall = []
        for i in range(12):
            rainfall.append(get_valid('Введите количество осадков в ' + str(i + 1) + ' месяце: '))
        return rainfall
    except:
        print('Ошибка получения данных')

def calc_and_print(rainfall):
    try:
        total = 0
        min_ = min(rainfall)
        min_index = rainfall.index(min_) + 1
        max_ = max(rainfall)
        max_index = rainfall.index(max_) + 1
        for i in rainfall:
            total += i
        average = total / 12
        print('Всего выпало осадков', total)
        print('В среднем осадков в месяц ', average)
        print('В', min_index, 'месяце выпало меньше всего осадков:', min_)
        print('В', max_index, 'месяце выпало больше всего осадков:', max_)
    except:
        print('Во время обработки данных произошла ошибка')
