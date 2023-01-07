inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
def func(x):
    x=x.lower()
    if x==x[::-1]:
        return True
    else:
        return False
sdsa=list(filter(func,inputdata))
print(sdsa)








