year = int(input('Enter year: '))
if (year % 400) == 0 or (year % 4) == 0:
    print('29')
else:
    print('28')
