import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = arr1.copy()

arr1[1] += 1

print(arr1.shape)
print(arr2)
