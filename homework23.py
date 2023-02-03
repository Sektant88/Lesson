class String(str):
    Stroka:str

    def __init__(self,Stroka:str):
        self.Stroka = str(Stroka)

    def __add__(self, other):
        other = str(other)
        print(self.Stroka+other)
        return String(self.Stroka+other)

    def __sub__(self, other):
        other = str(other)
        print(String(self.Stroka.replace(other, '', 1)))
        return String(self.Stroka.replace(other, '', 1))

String('New') + String(890)
String(1234) + 5678
String('New') + 'castle'
String('New') + True
String('New') + ['s', ' ', 23]
String('New') + None
print((type(String('New') + None)))



String('New bala7nce') - 7
String('New balance') - 'bal'
String('New balance') - 'Bal'
String('pineapple apple pine') - 'apple'
String('New balance') - 'apple'
String('NoneType') - None
String(55678345672) - 7
print(type(String('NoneType') - None))














