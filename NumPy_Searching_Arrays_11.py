##NumPy Searching Arrays

#Searching Arrays


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) 



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)


#Search Sorted

import numpy as np

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x) 


import numpy as np

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x) 


#Multiple Values


import numpy as np

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x) 