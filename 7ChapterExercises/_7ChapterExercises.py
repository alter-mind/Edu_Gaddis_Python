#импорт модулей для задач
import TotalSales
import LotteryNumberGenerator
import RainfallStatistics
import NumbersAnalysis
import ValidationAccountNumber
import MoreNumberN
import DriverExam
import SearchName
import PopulationData

#Главная функция. Показывает меню и вызывает нужные модули
def main():
    try:
        answer = 1
        while answer == 1:
            print_menu()
            module_selector(get_menu())
            answer = int(input('Для отображения меню и выбора задачи введите 1, для выхода 0:'))
    except:
        print('Может быть, следует почитать инструкции, перед тем, как нажимать на все кнопки?')

# Функция распечатки меню
def print_menu():
    print('--------------------------------\nВыберите задачу для запуска\n--------------------------------\n')
    print('1\tОбщий объём продаж')
    print('2\tГенератор лотерейных чисел')
    print('3\tСтатистика дождевых осадков')
    print('4\tПрограмма анализа чисел')
    print('5\tПроверка допустимости номера расходного счёта')
    print('6\tБольше числа n')
    print('7\tЭкзамен на получение водительских прав')
    print('8\tПоиск имени')
    print('9\tДанные о населении')

# Функция получения пользовательского выбора для запуска задачи
def get_menu():
    try:
        number = int(input('Задача для запуска: '))
        while not(number in range (1,13)):
            print('Такой задачи не существует')
            print_menu()
            number = int(input('Введите корректный номер задачи: '))
        return number
    except:
        print('Ошибочка. Нужно было указать номер')

# Функция, запускающая выбранный модуль/задачу
def module_selector(menu):
    if menu == 1:
        TotalSales.print_all()
    elif menu == 2:
        LotteryNumberGenerator.start()
    elif menu == 3:
        RainfallStatistics.calc_and_print(RainfallStatistics.get_rainfall_per_month())
    elif menu == 4:
        NumbersAnalysis.calc()
    elif menu == 5:
        ValidationAccountNumber.check_number()
    elif menu == 6:
        MoreNumberN.compare_and_print(MoreNumberN.get_n(), MoreNumberN.get_list())
    elif menu == 7:
        DriverExam.compare_and_print()
    elif menu == 8:
        SearchName.search()
    elif menu == 9:
        PopulationData.calc()
    else:
        print('Такой задачи ещё нет')


# Выполнение главной функции
main()