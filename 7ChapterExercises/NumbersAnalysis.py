def get_valid(message): #получение корректного числового значения
    try:
        value = float(input(message))
        return value
    except:
        print('Нужно было вводить число')
        return get_valid(message)

def calc():
    try:
        numbers = []
        total = 0
        for i in range(20):
            numbers.append(get_valid('Введите ' + str(i) + ' число: '))
            total += numbers[i]
        average = total / 20
        min_number = min(numbers)
        max_number = max(numbers)
        print('Cумма чисел ' + str(total) + '\n' +
              'Максимум ' + str(max_number) + '\n' +
              'Минимум ' + str(min_number) + '\n' +
              'Среднее ' + str(average))
    except:
        print('Ошибка. Что-то пошло не так')
