##NumPy Creating Arrays

#0-D Arrays

import numpy as np
arr = np.array(74)
print(arr) 


#1-D Arrays

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr) 



#2-D Arrays
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) 


#3-D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


#Higher Dimensional Arrays

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim) 
