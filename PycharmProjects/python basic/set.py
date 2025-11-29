p = {3,2,9,6,2,6,5,1}
print(p)

s1 = {2,5,8}
s2 = {5,6,8}
s3 = s1.intersection(s2)
print(s3)

g =[3,6,5,4,3,5,5,9,5,]
result=set(g)
print(result)

a = {1,2,3,4,5,6,}
b = {7,9,8}
result=a.union(b)
print(result)

p = {3,2,9,6,2,6,5,1}
p.add(66)
print(p)

p = {3,2,9,6,2,6,5,1}
p.update([55,888,99])
print(p)

p = {3,2,9,6,2,6,5,1}
p2 = {22,66,444,}
p.update([55,888,99],p2)
print(p)

p = {3,2,9,6,2,6,5,1}
p2 = {22,66,444,}
p.remove(2)
print(p)

s1 = {2,5,8}
s2 = {5,6,8}
s3 = s1.symmetric_difference(s2)
print(s3)

p = {5,10,15}
b = {20,25,30}
result=p.union(b)
print(result)