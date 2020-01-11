def get_data():
    try:
        file_name = 'USPopulation.txt'
        file = open(file_name,'r')
        pop_list = []
        for line in file:
            pop_list.append(float(line.rstrip()))
        file.close
        return pop_list
    except (IOError, ValueError):
        print('Файл отсутствует на диске, либо содержит неправильные данные. Взамен будет сгенерирован новый')
        gen_file(file_name)
        return get_data()


def gen_file(file_name):
    import random
    popolation = 153200
    file = open(file_name, 'w')
    for i in range(40):
        popolation += random.randrange(1,8000)
        file.write(str(popolation) + '\n')
    file.close
    print('Файл сгенерирован')

def calc():
    pop_list = get_data()
    pop_change_list = []
    average = 0
    for i in range(len(pop_list) - 1):
        pop_change_list.append(pop_list[i + 1] - pop_list[i])
        average += pop_change_list[i]
    average = average / len(pop_change_list)
    minimum = min(pop_change_list)
    maximum = max(pop_change_list)
    print('Среднее изменение численности населения: ', average, '\n',
          'Минимальное изменение численности населения:', minimum, '\n',
          'Максимальное изменение численности населения:', maximum)


