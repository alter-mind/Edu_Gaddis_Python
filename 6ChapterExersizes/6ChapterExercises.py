# импорт модулей
import PrintFile
import PrintFileTop
import LineNumbers
import NameCounter
import SumFileNumbers
import Mean
import RandomNumbersToFile
import ReadAndCountRandomNumbers
import GolfPoints
import PersonalWebPageCreator
import AverageSteps

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
    print('1\tПечать файла "numbers.txt"')
    print('2\tВывод на экран верхней части файла')
    print('3\tНомера строк')
    print('4\tСчётчик значений')
    print('5\tСумма чисел')
    print('6\tСреднее арифметическое')
    print('7\tПрограмма записи файла со случайными числами')
    print('8\tПрограмма чтения файлов со случайными числами')
    print('9\tОчки в игре в гольф (Запись)')
    print('10\tОчки в игре в гольф (Чтение)')
    print('11\tГенератор персональной веб-страницы')
    print('12\tСреднее количество шагов')

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
        print_file()
    elif menu == 2:
        print_file_top()
    elif menu == 3:
        line_numbers()
    elif menu == 4:
        name_counter()
    elif menu == 5:
        sum_numbers()
    elif menu == 6:
        mean()
    elif menu == 7:
        random_numbers_write()
    elif menu == 8:
        random_numbers_read()
    elif menu == 9:
        golf_points_write()
    elif menu == 10:
        golf_points_read()
    elif menu == 11:
        page_generator()
    elif menu == 12:
        average_steps()
    else:
        print('Видимо нет ещё такой задачи на выбор...')

# Функции, запускающие выполнение нужных модулей
def print_file():
    PrintFile.print_all()

def print_file_top():
    PrintFileTop.print_all()

def line_numbers():
    LineNumbers.print_all()

def name_counter():
    NameCounter.print_all()

def sum_numbers():
    SumFileNumbers.print_all()

def mean():
    Mean.print_all()

def random_numbers_write():
    RandomNumbersToFile.write_all()

def random_numbers_read():
    ReadAndCountRandomNumbers.print_all()

def golf_points_write():
    GolfPoints.write_all()

def golf_points_read():
    GolfPoints.read_all()

def page_generator():
    PersonalWebPageCreator.generate()

def average_steps():
    AverageSteps.calc()

# Выполнение главной функции
main()