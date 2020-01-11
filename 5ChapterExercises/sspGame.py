import random

def get_valid(message):
    value = int(input(message))
    while not((value > 0) and value <= 3):
        value = int(input('Введите корректное (целое, положительное) значение: '))
    return value

def play():
    print('Игра: "Камень, ножницы, бумага"')
    print('1\tкамень\n2\tножницы\n3\tбумага')
    person = get_valid('Введите Ваш выбор: ')
    bot = random.randint(1,3)
    if (bot == 1 and person == 1) or (bot == 2 and person == 2) or (bot == 3 and person == 3):
        print('ничья')
    elif (bot == 1 and person == 2) or (bot == 2 and person == 3) or (bot == 3 and person == 1):
        print('Вы проиграли')
    else:
        print('Вы выиграли')
