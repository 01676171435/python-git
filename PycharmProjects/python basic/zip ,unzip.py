
person_name = ['karim','nawaaz','tushar']
person_age =[23,25,27]

combine_two_list = list(zip('123',person_name , person_age))
print(combine_two_list)

all_info = [('1', 'karim', 23), ('2', 'nawaaz', 25), ('3', 'tushar', 27)]

unzip_all_info = list(zip(*all_info))
print(unzip_all_info)

a = ['malik','babul']
b = [24,25]
c = list(zip(b,a))
print(c)