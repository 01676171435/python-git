class person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def details(self):
        print(self.name ,self.age, sep='|')

p = person("musa" ,23)
p.details()

p = person("isqhe" ,23)
p.details()

