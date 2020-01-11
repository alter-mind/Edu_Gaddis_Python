days = int(input('Введите количество дней роста: ')) #ввод и ловушка ошибок 
while not(days>0):
    days = int(input('Такое количество дней невозможно. Введите верное количество дней: '))

percent = float(input('Введите прирост популяции в день в процентах: ')) #ввод и ловушка ошибок  
while not(percent in range(101)):
    percent = float(input('Такой процент невозможен. Введите корректный процентный прирост (0-100): '))

population = float(input('Введите начальную популяцию: ')) #ввод и ловушка ошибок 
while not(population > 0):
    population = float(input('Начальная популяция должна быть положительной. Введите корректное значение: '))

print('День\tПопуляция') # расчёт и вывод на экран
for day in range(days):
    population += population * percent / 100
    print(str(day + 1) + '\t' + str(population))
