future_money = float(input('Введите желаемую сумму: '))
rate = float(input('Введите годовую процентнтую ставку: '))
years = int(input('Введите срок вклада, лет: '))
current_money = future_money / (1 + rate)**years
print('Вам необходимо внести', current_money)