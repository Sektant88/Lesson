class auto(object):
    brand:str
    age:int
    mark:str
    weight:int
    color:str
    def __init__(self,brand:str,age:int,mark:str):
        self.brand=brand
        self.age=age
        self.mark=mark

    def move(self):
        self.move='move'
        print(self.move)
    def stop(self):
        self.stop='stop'
        print(self.stop)
    def birthday(self):
        self.birthday=self.age+1
        print('birthday: ',self.birthday)

camry=auto("toyota",2012,"camry")
print(camry.brand+" "+camry.mark+' '+camry.age.__str__())
camry.move()
camry.stop()
camry.birthday()





