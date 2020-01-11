p = 0
i = 0
t = 0

def get_valid(message):
    value = float(input(message))
    while not(value > 0):
        value = float(input('Введите корректное (положительное) значение: '))
    return value

def calc():
    global p
    global i
    global t
    p = get_valid('Введите текущую сумму на счёте: ')
    i = get_valid('Введите месячную процентную ставку: ')
    t = int(get_valid('Введите срок вклада в месяцах: '))
    p *= (1 + i)**t
    return p 
def print_all():
    print('На счёте будет', format(calc(), ',.2f'))
