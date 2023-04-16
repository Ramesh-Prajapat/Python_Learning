import numpy as np

num = np.array([1, 2, 3])
print(num)

## size all element will be count.
print(num.ndim)

## Change in one dimension to multiple dimension, whether our array/matrix is 2D or 3D or so on...
arr = np.array([[1,2,3], [4, 5, 6]])
flatten_arr = arr.flatten()
print(flatten_arr)