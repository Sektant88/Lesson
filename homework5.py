result = 0
number = int(input("Число: "))
while number > 0:
    if number % 3 != 0:
        result += number ** 3
    number -= 1
print(result)