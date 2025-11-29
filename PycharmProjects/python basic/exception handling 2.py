
def fantion(x,y):
    try:
        return x / y
        print("every thing is ok")

    except TypeError:
        print("you should not use string to divition")

print( fantion("30",2) )


def fantion(x,y):
    try:
        return x/y
        print("every thing is ok")

    except Exception as e:
        print("you can not use Zero to divition", e)

print(fantion(10,0))
