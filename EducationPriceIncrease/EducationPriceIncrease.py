INC = .07
YEARS = 5
price = 45000
print('Год \tСтоимость\n----------------\n' + str(1) + '\t' + str(price))
for year in range(2,YEARS + 1):
    price += price * INC
    print(str(year) + '\t' + str(format(price, ',.2f')))
