class auto(object):
    brand:str
    age:int
    mark:str
    weight=4
    color='black'
    def __init__(self,brand:str,age:int,mark:str):
        self.brand=brand
        self.age=age
        self.mark=mark
    
    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age+=1

camry=auto("toyota",2012,"camry")
print(camry.brand+" "+camry.mark)
print('color:',camry.color)
print('weight:',camry.weight)
print('age:',camry.age)
camry.birthday()
print('birthday:',camry.age)
camry.move()
camry.stop()





