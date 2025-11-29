import numpy as np
e1 = ([2,4,8],
      [4,7,6],
      [3,5,8]
      )

e2 = ([5,6,4],
      [4,7,3],
      [2,5,4]
      )
...
print(e1)
print(e2)
...

result = np.dot(e1 , e2)
print(result)