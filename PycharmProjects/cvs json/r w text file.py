''''
try:
    with open("code.txt") as fjob:      # to read a txt file
        contents = fjob.read()
        print(contents)

except Exception as e:
    print("file has error: " , e)

'''
with open("code.txt") as fjob:
    for num, line in enumerate(fjob):    #converting line with uppercase
        print( num+1 ,line.upper())

