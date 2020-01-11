speed = float(input('Введите скорость транспортного средства: '))
time = int(input('Введите время в пути: '))
print('Час\tПройденное расстояние')
print('_____________________________')
for t in range(1,time+1):
    print(t,'\t',speed*t)

