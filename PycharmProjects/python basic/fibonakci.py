# 0 1 1 2 3 5 8 13 21

def fibo(x):
    a = 0
    b = 1
    print(0)
    print(1)
    for i in range(2,x):
        c = a + b
        print(c)
        a = b
        b = c


fibo(10)

