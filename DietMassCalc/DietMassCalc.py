DELTA = 1.5
MONTH = 6
mass = float(input('Введите вашу массу: '))
while mass <= 0:
    mass = float(input('Масса не может быть нулевой или отрицательной. Введите вашу массу: '))
print('Месяц\tМасса\n---------------------')
for month in range(1,MONTH + 1):
    mass -= DELTA
    if mass <= 0:
        print('У вас недостаточная масса для этой диеты')
        break
    print(str(month) + '\t' + str(format(mass,'.1f')))
