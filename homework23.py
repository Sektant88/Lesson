class String(str):
    Stroka:str

    def __init__(self,Stroka:str):
        self.Stroka = Stroka

    def __str__(self):
        Stroka=self.Stroka+self.Stroka
        return Stroka

    def __sub__(self, other):
        return self.Stroka.replace(other,'')


rob = String('vasya')
bob = String('pupkin')
plus = rob + bob
print(plus)

dar = String('new')
gap = String(86)
plus_1 = dar+gap
print(plus_1)

tema = String('six')
arem = String(None)
plus_2 = tema + arem
print(plus_2)

sam = String('zero')
ams = String(True)
plus_3 = sam + ams
print(plus_3)

delo=String('fdas')
loft=String([2,'ddfs',''])
plus_4 = delo + loft
print(plus_4)



god = String('new balance')
dog = String('bala')
minus = god-dog
print(minus)

ser=String('new balan7ce')
res=String('7')
minus_1 = ser-res
print(minus_1)










