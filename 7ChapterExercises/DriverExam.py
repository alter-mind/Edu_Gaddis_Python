def generate_student_file(): # Создание файла с ответами студента
    try:
        answer = input('Хотите ввести ответы теста самостоятельно? 1 - да, остальное - нет: ')
        file = open('student_solution.txt','w')
        if answer == '1':
            for i in range(20):
                file.write(input('Введите ответ на ' + str(i+1) + ' вопрос: ') + '\n')
        else:
            import random
            for i in range(20):
                test_answer = random.randrange(0,4)
                if test_answer == 0:
                    file.write('A' + '\n')
                elif test_answer == 1:
                    file.write('B' + '\n')
                elif test_answer == 2:
                    file.write('C' + '\n')
                else:
                    file.write('D' + '\n')
    except:
        print('Создание файла завершилось ошибкой')
    finally:
        file.close

def compare_and_print():
    try:
        file = open('student_solution.txt','r')
        answers_list = create_answers_list()
        student_list = []
        for line in file:
            student_list.append(line.rstrip('\n'))
        wrong_list = []
        for i in range(20):
            if answers_list[i] != student_list[i]:
                wrong_list.append(i+1)
        if len(wrong_list) <= 5:
            print('Экзамен сдан')
        else:
            print('Экзамен не сдан')
        print('Правильных ответов: ' + str(20 - len(wrong_list)))
        print('Неправильных ответов: ' + str(len(wrong_list)) + ' Вопросы, на которые ответ не верный: ' + str(wrong_list))
    except IOError:
        print('Файл student_sulution.txt не найден')
        answer = input('Хотите создать файл? 1 - да, всё остальное - нет: ')
        if answer == '1':
            generate_student_file()
        compare_and_print()
    except:
        print('Что-то пошло не так')

def create_answers_list():
    answers_list = []
    answers_list.append('A')
    answers_list.append('C')
    answers_list.append('A')
    answers_list.append('A')
    answers_list.append('D')
    answers_list.append('B')
    answers_list.append('C')
    answers_list.append('A')
    answers_list.append('C')
    answers_list.append('B')
    answers_list.append('A')
    answers_list.append('D')
    answers_list.append('C')
    answers_list.append('A')
    answers_list.append('D')
    answers_list.append('C')
    answers_list.append('B')
    answers_list.append('B')
    answers_list.append('D')
    answers_list.append('A')
    return answers_list
