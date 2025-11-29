
class X:
   def __init__(self, name):
       self.name = name
       print(self.name + "created")

   def details(self):
      print(self.name + "destroyd" )


x = X("X")
y = X("Y")
x.details()
y.details()
print("Hello world")


