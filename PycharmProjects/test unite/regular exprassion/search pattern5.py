'''
import re
data =  '15/Fedary/1975 was the high time to kil'  #  r' alternative is //

if re.match('\\d+/[a-zA-z]+/\\d{4}', data):
    print("matched")

else:
    print('mismatched')
'''

import re

data =  '15/Fed/1975 i will go to canada'
data_pattern =\
re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')
print("Before:", data)

date_modify = data_pattern.sub(r'\3-\2-\1',data)    #date side convert
print("after:", date_modify )