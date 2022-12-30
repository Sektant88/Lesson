while True:
    name = input('Ваше имя:')
    age =input('Ваш возраст:')
    if not age.isdigit() or age < 0:
        print('ошибка повторите ввод')

    elif 0 < age < 10:
        print('привет шкет', name)
    elif 10 <= age <= 18:
        print('как жизнь', name)
    elif  18 < age < 100:
        print('что желате,',name)
    elif age > 100:
         Print('вы врете,в наше время столько не живут')
    answer = input('желаете продолжить Y-НЕТ Д-ДА: ')
    if answer.upper() in ('У','Д'):
        break
