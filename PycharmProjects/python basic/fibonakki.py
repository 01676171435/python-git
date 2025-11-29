

def fibonaki(x):
    a = 2
    b = 4
    print(0)
    print(1)
    for i in range(2,x):
        c=a+b
        a=b
        b=c
        print(c)
fibonaki(10)