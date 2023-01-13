def func():
    a=int(input('введите число: '))
    if a % 2 ==0:
        print('четное')
    else:
        print('не четное')

def func_2():
    result = 0
    number = int(input("Число: "))
    while number > 0:
        if number % 3 != 0:
            result += number ** 3
        number -= 1
    print(result)


def decorator(func,func_2):
    def wrapper():
        from datetime import datetime
        time = datetime.now()
        func()
        durationTimed_1 = datetime.now()  - time
        print('время ф-кции: ',durationTimed_1)
        func_2()
        durationTimed_2 = datetime.now() - time
        print('время 2-ой ф-кции: ',durationTimed_2)

    return wrapper()
decorator(func,func_2)
