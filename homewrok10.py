def func():
    import random
    try_1=0
    secret=random.randint(0,15)
    while try_1 < 5:
        number=int(input('Введите число: '))
        if number < secret:
             print('число меньше загаданного')
        elif number > secret:
            print('число больше загаданного')
        else:
            print(f"вы угадали число {secret}")
            break
        try_1+=1
    else:
        print(f"число {secret} так и не было угадано")
func()




