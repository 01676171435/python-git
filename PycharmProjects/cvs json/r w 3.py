with open("number.txt" ,'w') as fjob:    # adding a new file with taxt in the file
    fjob.write('5')
    fjob.write('\n')
    fjob.write('93333')

with open("message.txt", 'a') as fjob:  # adding a new file with adding  a massage with  exiting massage
    fjob.write("life is beautiful \n")



import os
if os.path.exists("number.txt"):   # to find a exiting file in the hardisk
    print("yes, file exits")

