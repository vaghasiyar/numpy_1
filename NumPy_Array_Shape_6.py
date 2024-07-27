##NumPy Array Shape


#Get the Shape of an Array

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) 


#The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)