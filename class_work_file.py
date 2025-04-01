# 1. Importing NumPy
import numpy as np

# 2. Creating Arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

print("Shape:", arr2.shape)        # (2 rows, 3 columns)
print("Dimensions:", arr2.ndim)    # 2D array
print("Data Type:", arr1.dtype)    # int64 or int32

print("First element of arr1:", arr1[0])
print("First row of arr2:", arr2[0])
print("Element at (1,2):", arr2[1, 2])
