speed = float(input('Enter speed: '))
if speed >= 0 and speed <= 200:
    print('Ok')
elif speed > 200:
    print('Not so fast!')
else:
    print('Uncorrect speed')
