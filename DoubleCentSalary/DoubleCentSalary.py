days = int(input('Введите количество рабочих дней: '))
money = 1
for i in range(days):
    money *= 2
money_rub = money // 100
money = money % 100
print('Ваша зарплата составит ', money_rub, 'рублей', money, 'копеек')
