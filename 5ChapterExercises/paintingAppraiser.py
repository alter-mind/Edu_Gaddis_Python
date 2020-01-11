COST = 2000
HOURS = 8
LITRES = 5
SQUARE = 10

def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    square = get_valid('Введите площадь окрашиваемой поверхности: ')
    price = get_valid('Введите стоимость 5 литров краски: ')
    if square % SQUARE == 0:
        paint_bottles = square // SQUARE
    else:
        paint_bottles = square // SQUARE + 1
    work_hours = square / SQUARE * 8
    paint_price = paint_bottles * price
    work_price = square / SQUARE * COST
    total_price = paint_price + work_price
    print('Количество требующихся ёмкостей краски:',paint_bottles)
    print('Количество требующихся рабочих часов:', work_hours)
    print('Стоимость краски:', paint_price)
    print('Стоимость работы:', work_price)
    print('Общая стоимость малярных работ:', total_price)