from linked import Doublelinkedlist

class Stuck:
    def __init__(self):
        self.__list = Doublelinkedlist()

    def push(self):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val


    def  is_empty(self):
        return self.__list.size ==0

    def peek(self):
        return self.__list.back()
    def __len__(self):
        return self.__list.size

my_stuck = Stuck()
my_stuck.push(1)
my_stuck.push(2)
my_stuck.push(3)
print(len(my_stuck))
