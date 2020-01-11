RUB = 100
KOP_5 = 5
KOP_10 = 10
KOP_50 = 50
DOL = 100
PENCE = 1
NICKEL = 5
DIME = 10
QUARTER = 25
flag = int(input('If you want play dollar game enter odd number, other for ruble game: '))
if (flag % 2) == 0:
    print('ruble game.\n You will be asked to choose the number of coins\n'
          + '5, 10 or 50 kopеcks. In total you need get 1 ruble.')
    kop5 = int(input('Enter number of 5 kopecks coins: '))
    kop10 = int(input('Enter number of 10 kopecks coins: '))
    kop50 = int(input('Enter number of 50 kopecks coins: '))
    money = kop5 * KOP_5 + kop10 * KOP_10 + kop50 * KOP_50
    if money == RUB:
        print('You win')
    elif money < RUB:
        print('You lose. Not enough')
    else:
        print('You lose. Too much')
else:
    print('dollar game. \n You will be asked to choose the number of coins\n'
          + 'pence, nickel, dime and quarter. In total you need get 1 dollar.')
    pence = int(input('Enter number of pence coins: '))
    nickel = int(input('Enter number of nickel coins: '))
    dime = int(input('Enter number if dime coins: '))
    quarter = int(input('Enter number of quarter coins: '))
    money = pence * PENCE + nickel * NICKEL + dime * DIME + quarter * QUARTER
    if money == DOL:
        print('You win')
    elif money < DOL:
        print('You lose. Not Enough')
    else:
        print('You lose. Too much')

