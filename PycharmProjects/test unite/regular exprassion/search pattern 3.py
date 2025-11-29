import re

data =  '15/Fedary/1975 15/Fedary/1975 ok 15/Fedary/1975 ' #matching all occurrence
data_pattern =re.compile(r'\d+/[a-zA-z]+/\d{4}')


result = data_pattern.findall(data)
print(result)