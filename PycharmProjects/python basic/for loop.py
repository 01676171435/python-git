a = ['cse','eee','science','math']
for dprt in a:
    print(dprt)


a = [10,20,30,40,50]
total=0
for i in a:
    total=total+i
print(total)

def factor(n):
    initial = 1
    for i in range(1,n+1):
        initial = initial * i
    return initial
result = factor(5)
print(result)

import math
n = 5
r = math.factorial(n)
print(r)

n = int(input('enter any value'))
f = 1
for i in range(1, n+1):
    f = f * i
print(f)

total =0
for i in range(1,11):
    total = total+i
print(total)