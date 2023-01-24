class auto(object):
    brand:str
    age:int
    mark:str
    weight:int
    color:str
    def __init__(self,brand:str,age:int,mark:str,color:str,weight:int):
        self.brand=brand
        self.age=age
        self.mark=mark
        self.color=color
        self.weight=weight
    
    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age+=1

camry=auto("toyota",2012,"camry","black",4)
print(camry.brand+" "+camry.mark+' '+' '+'color:',camry.color+', '+'weight: ',camry.weight.__str__())
print('age:',camry.age)
camry.birthday()
print('birthday:',camry.age)
camry.move()
camry.stop()





