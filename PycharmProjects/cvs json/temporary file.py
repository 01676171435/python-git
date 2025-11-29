
'''
from tempfile import TemporaryFile

with TemporaryFile('w+') as fobj:
    fobj.write('life is cool.\n')

    fobj.seek(8)
    data = fobj.read()
    print(data)
'''


import pickle

dict_data = {'name':'tushar','country':'Bangladesh'}

with open ('serialize','wb') as fodj:
    pickle.dump(dict_data, fodj)

with open('serialize', 'rb') as fodj:
    dict_data = pickle.load(fodj)
    print(dict_data)