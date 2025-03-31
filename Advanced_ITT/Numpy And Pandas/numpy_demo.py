# 1. Importing NumPy
import numpy as np

# 2. Creating Arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 3. Array Attributes
print("Shape:", arr2.shape)        # (2 rows, 3 columns)
print("Dimensions:", arr2.ndim)    # 2D array
print("Data Type:", arr1.dtype)    # int64 or int32

# 4. Indexing and Slicing
print("First element of arr1:", arr1[0])
print("First row of arr2:", arr2[0])
print("Element at (1,2):", arr2[1, 2])

# 5. Array Arithmetic
print("Add 5 to all elements:", arr1 + 5)
print("Square each element:", arr1 ** 2)
print("Element-wise addition:\n", arr2 + 10)

# 6. Aggregation Functions
print("Sum:", arr1.sum())
print("Max:", arr2.max())
print("Mean of arr2:", arr2.mean())

# 7. Reshaping and Transposing
arr3 = np.arange(12)              # [0 1 2 ... 11]
reshaped = arr3.reshape(3, 4)     # 3 rows, 4 columns
print("Reshaped Array:\n", reshaped)
print("Transposed:\n", reshaped.T)

# 8. Universal Functions (ufuncs)
print("Sqrt:", np.sqrt(arr1))
print("Log:", np.log(arr1))
print("Sin:", np.sin(arr1))

# 9. Random Number Generation
rand_array = np.random.randint(100, size=(3, 3))
print("Random 3x3 array:\n", rand_array)

# 10. Broadcasting Example
scalar = 10
broadcast_result = arr2 + scalar
print("Broadcasting (arr2 + 10):\n", broadcast_result)
