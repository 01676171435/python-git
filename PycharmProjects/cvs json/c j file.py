list_items = [['name','age','country'],
              ['bill gates',55,'us'],
              ['mark',34,'us'],
              ['swift',35,'canada']
              ]


import  csv

with open('people.csv', 'w') as fobj:
    fcsv= csv.writer(fobj)
    fcsv.writerows(list_items)