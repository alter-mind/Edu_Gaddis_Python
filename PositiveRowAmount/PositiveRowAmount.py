amount = 0
number = 0
while number >= 0:
    number = float(input('Введите положительное число, чтобы добавить его в сумму ряда, отрицательное, чтобы завершить программу: '))
    amount += number
print('Cумма ряда:',format(amount, '.2f'))
