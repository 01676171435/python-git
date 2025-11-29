
a = 25

b = 0

try:
    print("Resource open")
    print(a/b)          # if try`s code is worked then python will take input                                            will take input
    n = int(input("enter any number : "))
except ZeroDivisionError:
  print(" you can not divided a number by 0")
except ValueError :
  print('something is wrong ')

finally:
    print("resource close")
print('ok buy')


x = 12
y = 0

try:
   print(x/y)
except Exception as e:                #Exception is used for all type error
    print("zero is not divicible",e)  #e is used for knowing the type
print('ok buy')
