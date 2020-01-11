#импорт модулей
import KilometerConverter
import salesTax
import insuranceCalc
import carExpenses
import propertyTax
import caloriesFatCarbCalc
import stadiumSeats
import paintingAppraiser
import monthSalesTax
import feetToInches
import testMath
import maxTwo
import fallHeight
import kineticEnergy
import GPAandLavel
import oddEvenNumberCounter
import isPrime
import isPrimeAdvanced
import depositCalc
import guessingGame
import sspGame

#основная функция
def main():
    answer = 1
    while answer == 1:
        print_menu()
        module_selector(get_menu())
        answer = int(input('Для отображения меню и выбора задачи введите 1, для выхода 0:'))

#выбор модуля для запуска
def module_selector(menu):
    if menu == 1:
        kilometer_konverter()
    elif menu == 2:
        sales_tax()
    elif menu == 3:
        insurance_calc()
    elif menu == 4:
        car_expenses()
    elif menu == 5:
        property_tax()
    elif menu == 6:
        calories()
    elif menu == 7:
        stadium_seats()
    elif menu == 8:
        painting_appraiser()
    elif menu == 9:
        month_sales_tax()
    elif menu == 10:
        feet_to_inches()
    elif menu == 11:
        math_test()
    elif menu == 12:
        max_two()
    elif menu == 13:
        fall_height()
    elif menu == 14:
        kinetic_energy()
    elif menu == 15:
        GPA_and_lavel()
    elif menu == 16:
        even_odd_counter()
    elif menu == 17:
        is_prime()
    elif menu == 18:
        prime_list()
    elif menu == 19:
        deposit_calc()
    elif menu == 20:
        play_random()
    elif menu == 21:
        ssp_game()
    else:
        print('Такой задачи пока нет')
    

#функция вывода меню на экран
def print_menu():
    print('--------------------------------\nВыберите задачу для запуска\n--------------------------------\n')
    print('1\tКонвертер километров')
    print('2\tМодернизация программы рассчёта налога с продаж')
    print('3\tСтоимость страховки')
    print('4\tРасходы на автомобиль')
    print('5\tНалог на недвижимое имущество')
    print('6\tКалории за счёт жиров и углеводов')
    print('7\tСидячие места на стадионе')
    print('8\tОценщик малярных работ')
    print('9\tМесячный налог с продаж')
    print('10\tФуты в дюймы')
    print('11\tМатематический тест')
    print('12\tМаксимальное из двух значений')
    print('13\tВысота падения')
    print('14\tКинетическая энергия')
    print('15\tСредний балл и его уровень')
    print('16\tСчётчик чётных/нечётных чисел')
    print('17\tПроверка на простоту')
    print('18\tСписок простых чисел')
    print('19\tБудущая стоимость')
    print('20\tИгра в угадывание случайного числа')
    print('21\tКамень ножницы бумага')


# функция получения и валидации пункта меню
def get_menu():
    number = int(input('Задача для запуска: '))
    while not(number in range (1,22)):
        print('Такой задачи не существует')
        print_menu()
        number = int(input('Введите корректный номер задачи: '))
    return number

#функция модуля для задачи 1
def kilometer_konverter():
    print('В пересчёте на мили: ' + str(KilometerConverter.convert()))

#функция модуля для задачи 2
def sales_tax():
    salesTax.print_all()

#функция модуля для задачи 3
def insurance_calc():
    insuranceCalc.print_all()

#функция модуля для задачи 4
def car_expenses():
    carExpenses.calc()

#функция модуля для задачи 5
def property_tax():
    popertyTax.calc()

#функция модуля для задачи 6
def calories():
    caloriesFatCarbCalc.calc()

#функция модуля для задачи 7
def stadium_seats():
    stadiumSeats.calc()

#функция модуля для задачи 8
def painting_appraiser():
    paintingAppraiser.calc()

#функция модуля для задачи 9
def month_sales_tax():
    monthSalesTax.print_all()

#функция модуля для задачи 10
def feet_to_inches():
    feetToInches.calc()

# функция модуля для задачи 11
def math_test():
    testMath.start_test()

# функция модуля для задачи 12
def max_two():
    maxTwo.calc()

# функция модуля для задачи 13
def fall_height():
    fallHeight.calc()

# функция модуля для задачи 14
def kinetic_energy():
    kineticEnergy.calc()

# функция модуля для задачи 15
def GPA_and_lavel():
    GPAandLavel.print_all()

# функция модуля для задачи 16
def even_odd_counter():
    oddEvenNumberCounter.gen_and_count()

# функция модуля для задачи 17
def is_prime():
    isPrime.calc()

# функция модуля для задачи 18
def prime_list():
    isPrimeAdvanced.print_all()

# функция модуля для задачи 19
def deposit_calc():
    depositCalc.print_all()

# функция модуля для задачи 20
def play_random():
    guessingGame.play()

# функция модуля для задачи 21
def ssp_game():
    sspGame.play()

main()