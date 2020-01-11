print('Reboot your PC and try connect again')
answer = input('You fixed the problem?\n')
if not(answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА'):
    answer = input('Reboot your router and try connect agian. \nYou fixed the problem?\n')
    if not(answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА'):
        answer = input('Check the power cable of the router. \nYou fixed the problem?\n')
        if not(answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА'):
            answer = input('Check the cable connecting betwen router and modem.\nYou fixed problem?\n')
            if not(answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА'):
                answer = input('Move the router to the new location\nYou fixed problem?\n')
                if not(answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА'):
                    print('Holy shit. Call the police immediately!')