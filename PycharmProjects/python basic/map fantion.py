
...
def function(number):
    return number * 5
result = []
num =[5,8,9,9,7]
for i in num:
    result.append(function(i))
print(result)
...




def function(number):
    return number * 5
num =[5,8,9,9,7]
list(map(function,num))
print(list(map(function,num)))

