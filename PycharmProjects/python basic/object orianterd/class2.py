class person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def details(self):
        print(self.name ,self.age, sep='|')

people_list = []
for x in range(0,3):
    p = person("ibrahim"+str(x), 30+x)
    people_list += [p]

for x in people_list:
    x.details()