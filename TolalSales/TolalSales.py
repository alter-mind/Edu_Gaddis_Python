product1 = float(input('Enter 1 product price: '))
product2 = float(input('Enter 2 product price: '))
product3 = float(input('Enter 3 product price: '))
product4 = float(input('Enter 4 product price: '))
product5 = float(input('Enter 5 product price: '))
TAX = .07
total_price = product1 + product2 + product3 + product4 + product5
total_tax = total_price * TAX
total_bill = total_price + total_tax
print('Total price:', format(total_price, ',.2f'), 'Total tax:', format(total_tax, ',.2f'), 'Total bill', format(total_bill, ',.2f'))
