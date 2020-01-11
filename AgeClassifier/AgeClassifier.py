age = int(input('Enter age: '))
if age >= 0 and age <= 1:
    print('baby')
elif age > 1 and age < 13:
    print('child')
elif age >=13 and age < 20:
    print('teenager')
elif age > 20 and age < 100:
    print('adult')
elif age >= 100 and age < 150:
    print('wow')
elif age >= 150:
    print('impossible')
else:
    print('err. No one could have negative age')
