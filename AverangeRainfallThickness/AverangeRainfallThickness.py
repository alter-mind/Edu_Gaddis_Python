YEASRS = 5
MONTHS = 12
def get_rainfall(year,month):
    print('Введите количество осадков в ', month +1 ,' Месяце ', year + 1, ' года:')
    return float(input(''))
month_sum = 0
rainfall_sum = 0
for year in range(YEASRS):
    for month in range(MONTHS):
        rainfall_sum += get_rainfall(year, month)
        month_sum += 1
averange_rainfall = rainfall_sum / month_sum
print('Всего осадков:', format(rainfall_sum, '.2f'), 'Всего месяцев:', month_sum, 'Среднемесячное количество осадков:', format(averange_rainfall, '.2f'))
