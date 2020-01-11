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

def get_week_sales(): #создание и заполнение списка значениями
    try:
        week_sales = []
        for i in range(7):
            week_sales.append(get_valid('Введите продажи за ' + str(i + 1) + ' день недели: '))
        return week_sales
    except:
        print('Что-то пошло не так. Ошибка функции get_week_sales() в модуле TotalSales.py')

#вычисление суммы продаж за неделю
def calc(week_sales):
    try:
        sum = 0
        for i in week_sales:
            sum += i
        return sum
    except:
        print('Что-то пошло не так. Ошибка при вычислении общей суммы продаж')

#вывод результатов работы модуля
def print_all():
    print('Общая сумма продаж: ' + str(calc(get_week_sales())))