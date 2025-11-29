class Emplyee:
    salary = 20

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fantion1(self,worker):
        self.w = worker

    def fantion2(self,manager):
        self.m = manager

object = Emplyee('tushar',30)
object.fantion1(10)
print(object.w)
object.fantion2(15)
print(object.m)
print(object.name)