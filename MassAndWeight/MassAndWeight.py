mass = float(input('Enter mass: '))
weight = mass * 9.8
if weight >= 0 and weight < 100:
    print('too light')
elif weight >= 100 and weight <= 500:
    print('ok')
elif weight > 500:
    print('too heavy')
else:
    print('error')