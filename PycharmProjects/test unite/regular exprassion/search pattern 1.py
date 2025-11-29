import re

data =  '15/Fedary/1975 was the high time to kil'  # to match the data

if re.match(r'\d+/[a-zA-z]+/\d{6}', data):
    print("matched")

else:
    print('mismatched')