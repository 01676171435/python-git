
p1 = {'malik': 3, 10:10,10.2:6,True:False}
print(p1)

p1 = {'malik': 3, 10:10,10.2:6,True:False}
print(p1[10])

a1 = {'malik': 3, 10:10,10.2:6,True:False}
a1['variable'] = 'kala'
print(a1)

d1 = {"tushar":27,"karim":25,"nawaz":20}
d2 = d1.copy()
print(d2)

p1 = {'malik': 3, 10:10,10.2:6,True:False}
p1.pop('malik')
print(p1)
# nasted dictonary

d2 = {1:{ 2:"nawaz", 3:"Karim"},
      2:{2:"jamal", 3:"kamal"}}
print(d2[2][2])
print(d2[1][2])

d2[3]={}
d2[3]["elon"] = "tasla"
d2[3]["mark"] = "facebook"

print(d2[3])
del d2[3]['elon']
print(d2)