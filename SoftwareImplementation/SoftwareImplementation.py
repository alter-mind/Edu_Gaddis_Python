DEFAULT_PRICE = 99
number_of_pockets = int(input('Enter number of pockets you wish to bue: '))
if number_of_pockets < 0:
    print('You cant bue negative number of pockets')
    discount = 1
elif number_of_pockets in range(0,10):
    discount = 0
elif number_of_pockets in range(10,20):
    discount = .10
elif number_of_pockets in range(20,50):
    discount = .20
elif number_of_pockets in range(50,100):
    discount = .30
else:
    discount = .40
if discount != 1:
    total_price = DEFAULT_PRICE * number_of_pockets * (1 - discount)
    total_discount = DEFAULT_PRICE * number_of_pockets * discount
    print('Price:',format(total_price, ',.2f'), '\nDiscount:', format(total_discount, ',.2f'))
