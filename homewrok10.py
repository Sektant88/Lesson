def func():
    import random
    try_1=0
    secret=random.randint(0,15)
    while try_1 < 5:
        number=input('Введите число: ')
        if number.isdigit():
            number = int(number)
        else:
            print('ошибка,это не число,заново!')
        if number > secret:
             print('число меньше загаданного')
        elif number < secret:
            print('число больше загаданного')
        else:
            print(f"вы угадали число {secret}")
            break
        try_1+=1
    else:
        print(f"ха-ха,не угадали это число: {secret} ")
func()




