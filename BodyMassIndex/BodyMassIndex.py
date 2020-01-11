mass = float(input('Mass(kg): '))
height = float(input('Height(meters): '))
bmi = mass / height ** 2
if bmi < 18.5:
    print('mass min, bmi:', format(bmi, '.2f'))
elif bmi >=18.5 and bmi <= 25:
    print('normal mass, bmi:', format(bmi, '.2f'))
else:
    print('mass to much, bmi:', format(bmi, '.2f'))