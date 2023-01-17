def check_str(number:str)->str:
    if number.find('-') != -1:
        if number.find('-') == number.rfind('-') and number.find('-') == 0:
            if (number.find('.') == number.rfind('.') and number.rfind('.') != -1) \
                    or (number.find(',') != -1 and number.find(',') == number.rfind(',')):
                return "отрицательное дробное"

            else:
                return "отрицательное целое "

        else:
            return "неправильное число"

    elif number.find('.') != -1 or number.find(',') != -1:
        if number.find('.') != -1:
            count = 0
            a = number.split('.')
            for item in a:
                for i in range(1, 10):
                    if item.find(str(i)) != -1:
                        count += 1
            if count == 0:
                return "нули"
        if number.find(',') != -1:
            count = 0
            a = number.split(',')
            for item in a:
                for i in range(1, 10):
                    if item.find(str(i)) != -1:
                        count += 1
            if count == 0:
                return "нули"

        if (number.find('.') == number.rfind('.') and number.find('.') != -1) \
            or (number.find(',') != -1 and number.find(',') == number.rfind(',')):
            return 'дробное'
        else:
            return 'неправильное число'
    else:
        return "неправильное число"
while True:
        number = input('введите число: ')
        if number.lower() in ('q','exit','quit','выход','e'):
            break

        if number.isdigit():
            print('целое число')
        else:
            print(check_str(number))


