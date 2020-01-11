def C_to_F(cel):
    return 9/5 * cel + 32
start = int(input('Введите начальную температуру: '))
end = int(input('Введите конечную темперетуру: '))
step = int(input('Введите шаг: '))
print('C\tF')
for temp in range(start, end + 1, step):
    print(str(temp) + '\t' +  str(format(C_to_F(temp),'.1f')))
