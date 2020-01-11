total = 0
budget = float(input('Введите сумму, выделенную на месяц: '))
sum = 0
def selector():
    select = int(input('Введите 1 для продолжения, 0 - для выхода: '))
    if select == 1:
        return True
    else:
        return False
while selector():
    sum += float(input('Введите расход по отдельной статье: '))
if total > sum:
    print('Вы съэкономили:',format(total - sum, ',.2f'))
elif total < sum:
    print('Перерасход:',format(sum - total, ',.2f'))
else:
    print('Вы точно уложились в бюджет')
