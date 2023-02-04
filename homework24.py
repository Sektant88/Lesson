class Myclass():
    a=100
    def __init__(self,a:int):
        self.a=a


    def __add__(self, other):
        return self.a+other.a

    def __truediv__(self, other):
      return self.a / other.a

    @staticmethod
    def zorro(d):
        return d.a * 2

    @staticmethod
    def sanji(b):
        return b.a**2

    @classmethod
    def chopper(cls):
        return cls.a-20




obj=Myclass(10)
fjd=Myclass(20)

a=obj.zorro(obj)
print(a)

b=obj.sanji(obj)
print(b)

plus=obj+fjd
print(plus)

gg=fjd / obj
print(gg)

c=obj.chopper()
print(c)




