x = 50

def ac():
    y = x+50
    print('inside =',y)
ac()

print('outside' ,x )

def fan():
    global x
    x = x+150
    print('update global',x )
fan()