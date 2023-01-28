import time


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
class car(auto):
    max_speed:int
    def __init__(self,brand:str,age:int,mark:str,max_speed:int):
        super().__init__(brand,age,mark)
        self.max_speed=max_speed
    def move(self):
        super().move()
        print("max speed is ",self.max_speed)

class truck(auto):
    max_load:int

    def __init__(self, brand: str, age: int, mark: str, max_load:int):
        super().__init__(brand,age,mark)
        self.max_load=max_load

    def move(self):
        print('attetion')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

Man=truck("Man",2014,'bizon',234)
print(Man.brand+' '+Man.mark+' '+Man.age.__str__()+' '+'max load: ',Man.max_load.__str__())
Man.move()
Man.load()
lamborgini=car("Lamborgigni",2019,'Aventador',400)
print(lamborgini.brand+' '+lamborgini.mark+' '+lamborgini.age.__str__())
lamborgini.move()


