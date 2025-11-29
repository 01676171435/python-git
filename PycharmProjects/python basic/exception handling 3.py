a = 25

b = 0

try:
    print(a / b)
except:
    pass          # pass mean nobody can see error
else:
    print("every thing is ok" )



def div(x,y):
    return x / y
try:
    div_result = div(8,0)
except:
    print("divisible by zero is not possible")
else:
    print("div result is" +str(div_result))