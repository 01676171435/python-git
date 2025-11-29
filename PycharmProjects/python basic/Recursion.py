import sys
print('limit =' ,sys.getrecursionlimit())
sys.setrecursionlimit(1500)
count = 0
def funtion():
    global  count
    count = count+1
    print("elon mask",count)
    funtion()
funtion()
