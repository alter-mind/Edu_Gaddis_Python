number = int(input('Enter number: '))
if number in range(37):
    if number == 0:
        print('green')
    elif number in range(1,11):
        if (number % 2) == 0:
            print('black')
        else:
            print('red')
    elif number in range(11,19):
        if (number % 2) == 0:
            print('red')
        else:
            print('black')
    elif number in range(19,29):
        if (number % 2) == 0:
            print('black')
        else:
            print('red')
    elif number in range(29,37):
        if (number % 2) == 0:
            print('red')
        else:
            print('black')
else:
    print('error: wrong number')