import re

data =  '15/Fedary/1975 was the high time to kil'  #to match the data
data_pattern =re.compile(r'\d+/[a-zA-z]+/\d{3}')


if data_pattern.match(data):
    print("matched")

else:
    print('mismatched')