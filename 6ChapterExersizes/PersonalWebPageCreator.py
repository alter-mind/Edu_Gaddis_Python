def generate():
    try:
        file_name = input('Введите назвение веб - страницы: ') + '.html'
        file = open(file_name, 'w')
        file.write('<html>' + '\n')
        file.write('<head>' + '\n')
        file.write('</head>'+ '\n')
        file.write('<body>'+ '\n')
        file.write('  <center>'+ '\n')
        file.write('  <h1>' + input('Введите своё имя: ') + '</h1>'+ '\n')
        file.write('</center>'+ '\n')
        file.write('  <hr />' + '\n')
        file.write(input('Опишите себя: ') + '\n')
        file.write('  <hr />' + '\n')
        file.write('</body>' + '\n')
        file.write('</html>' + '\n')
        file.close()
        print('страница ' + file_name + ' создана' + '\n')
    except:
        file.close()
        print('Что-то пошло не так. Не удалось создать страницу')