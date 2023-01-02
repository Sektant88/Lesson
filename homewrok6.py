value=1
result=0
number=int(input("Введите число: "))
for item in range(value, number+1):
    if item % 3 != 0:
        result += item ** 3
print(result)