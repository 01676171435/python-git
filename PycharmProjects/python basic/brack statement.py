'''
n = int(input('How maney iphone do you need'))
i = 1

while i <=n:
     print('iphon',i)
     i = i + 1
print('ok thank')
'''
availavail = 5
n = int(input('How maney iphone do you need'))

i = 1

while i <=n:
    if i >availavail:
        break
    print('iphon',i)
    i = i+1



print('ok thank')