FED = .05
REG = .025
cost = 0
def get_valid_cost():
    cost = float(input('Введите величину продаж за месяц: '))
    while not(cost > 0):
        cost = float(input('Введите корректную (положительную) величину: '))
    return cost

def fed_tax():
    return cost * FED 

def reg_tax():
    return cost * REG 

def total_tax():
    return fed_tax() + reg_tax()

def print_all():
    get_data()
    print('Федеральный налог: ' + str(fed_tax()))
    print('Региональный налог: ' + str(reg_tax()))
    print('Общая сумма налога: ' + str(total_tax()))

def get_data():
    global cost
    cost = get_valid_cost()

