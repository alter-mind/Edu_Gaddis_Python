distance = float(input('Enter distance: '))
consumption = float(input('Enter gas consumption per 100 km: '))
total_consumption = distance / 100 * consumption
print('Total gas consumption:', format(total_consumption, ',.2f'))
