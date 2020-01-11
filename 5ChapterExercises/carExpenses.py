def calc():
    credit = float(input('Введите ежемесячный платёж по автокредиту: '))
    while not(credit > 0):
        credit = float(input('Введите корректное (положительное) значение: '))
    insurance = float(input('Введите сумму ежемесячной страховки авто: '))
    while not(insurance > 0):
        insurance = float(input('Введите корректное (положительное) значение: '))
    gas = float(input('Введите сумму месячных расходов на бензин: '))
    while not(gas > 0):
        gas = float(input('Введите корректное (положительное) значение: '))
    engine_oil = float(input('Введите месячные расходы на моторное масло: '))
    while not(engine_oil > 0):
        engine_oil = float(input('Введите корректное (положительное) значение: '))
    tires = float(input('Введите месячные расходы на шины: '))
    while not(tires > 0):
        tires = float(input('Введите корректное (положительное) значение: '))
    maintenanse = float(input('Введите месячные расходы на техобслуживание: '))
    while not(maintenanse > 0):
        maintenanse = float(input('Введите корректное (положительное) значение: '))
    month = credit + insurance + gas + engine_oil + tires + maintenanse
    year = month * 12
    print('Месячные расходы на автомобиль:',month)
    print('Годовые расходы на автомобиль:',year)
