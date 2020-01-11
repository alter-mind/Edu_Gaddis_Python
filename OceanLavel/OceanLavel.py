DELTA = 1.6
YEARS = 25
print('Год \t уровень океана \n-------------------------------')
for year in range(1, YEARS + 1):
    lavel = DELTA * year
    print(str(year) + '\t' + str(format(lavel, '.1f')))
