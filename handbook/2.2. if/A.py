username = input()
q = input()
print('Как вас зовут?')
print(f'Здравствуйте, {username}!')
print('Как дела?')

match q:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')
    case _:
        print('Я не знаю ответа на этот вопрос!')
