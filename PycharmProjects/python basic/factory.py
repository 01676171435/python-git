def funtion(n):
    initial= 1
    for i in range(1,n+1):
        initial = initial * i
    return initial
result = funtion(5)
print(result)

n = int(input('enter any nubmer'))
f = 1
for i in range(1,n+1):
    f = f * i

print(f)