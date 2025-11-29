

class MsName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name
        self.last_name           #self.last_name is not working in unite test

m1 = MsName('manik',"koli")
m1.full_name()