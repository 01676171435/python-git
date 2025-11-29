import re

data =  '15/Fed/1975 i will go to canada'
data_pattern =\
re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')


result = data_pattern.match(data)

for x in range(0, 4):
    print (result.groups(x))

print(result.groups())

day, month, year = result.groups()
print("Today day is", day)