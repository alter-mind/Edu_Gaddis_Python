n = int(input('Введите натуральное число:'))
if not(n>0):
    n = int(input('Вы ввели не натуральное число, введите натуральное число: '))
factorial = 1
for n in range(1, n+1):
    factorial *= n
print('Факториал ' + str(n) + ': ' + str(factorial))