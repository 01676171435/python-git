
class math:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x+self.y

math_Object = math(9,6)
print(math_Object.sum())
