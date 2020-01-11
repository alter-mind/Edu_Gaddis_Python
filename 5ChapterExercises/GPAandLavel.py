ITERATIONS = 5
def get_valid(message):
    value = int(input(message))
    while not(value in range(0,101)):
        value = float(input('Введите корректное (от 0 до 100) значение: '))
    return value

def calc_average():
    average = 0
    for i in range(ITERATIONS):
        average += get_valid('Введите оценку в баллах от 0 до 100: ')
    average /= ITERATIONS
    average = int(average)
    return average

def determine_grade(average):
    if average in range (90,101):
        result = 'Уровель A, ' + str(average) + ' баллов.'
    elif average in range(80,90):
        result = 'Уровель B, ' + str(average) + ' баллов.'
    elif average in range(70,80):
        result = 'Уровель C, ' + str(average) + ' баллов.'
    elif average in range(60,70):
        result = 'Уровель D, ' + str(average) + ' баллов.'
    else:
        result = 'Уровель F, ' + str(average) + ' баллов.'
    return result

def print_all():
    print(determine_grade(calc_average()))

