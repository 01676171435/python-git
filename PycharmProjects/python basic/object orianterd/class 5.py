class math:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x+self.y

class math1(math):

    def __init__(self,x,y):
        super().__init__(x,y)

    def subtruction(self):
        return self.x-self.y

plase = math(3,6)
print(plase.sum() )

minus = math1(4,7)
print(minus.subtruction())

