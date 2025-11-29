from numpy import *

array1 = array([
    [2,3,5,6,8,9],
    [2,5,8,9,3,5]

])

print(array1.size)
array2 = array1.flatten()
print(array2)
array3 = array2.reshape(2,6)
print(array3)
array4 = array3.reshape(2,2,3)
print(array4)


import numpy as np

a = np.array([2,3, 4,6,8])

b = np.array([4,5,7,8,7])

c = a*b

print(c)