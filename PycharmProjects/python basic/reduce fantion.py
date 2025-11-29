import functools

def two(num1,num2):
    return num1+num2

list = [2,5,9,10]

result = functools.reduce(two ,list)
print(result)