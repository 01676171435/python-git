class person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def details(self):
        print(self.name ,self.age, sep='|')

bil = person("bill", 23)
bil.details()
print(bil.name,bil.age)





