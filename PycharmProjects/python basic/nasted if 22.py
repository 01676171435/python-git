x = int(input("inter 1st value"))
y = int(input("inter 2nd value"))
z = int(input("inter 3nd value"))

if x>y:
    if x>z:
        print('x is grather than y,z')
    else:
        print('z is grather than x,y')
elif y>x:
    if y>z:
        print('y is grather than x,z')
    else:
        print('z is grather than x,y')
