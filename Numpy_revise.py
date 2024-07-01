
import numpy as np


# 1D array
arr = np.array([1, 2, 3, 4])
print(arr)

# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)



# Array of zeros
zeros = np.zeros((2, 3))
print(zeros)

# Array of ones
ones = np.ones((3, 2))
print(ones)

# Array of a specific value
full = np.full((2, 2), 7)
print(full)

# Identity matrix
identity = np.eye(3)
print(identity)

# Random array
random_arr = np.random.random((2, 2))
print(random_arr)



# Using arange
arr = np.arange(0, 10, 2)  # start, stop, step
print(arr)

# Using linspace
arr = np.linspace(0, 1, 5)  # start, stop, number of values
print(arr)



arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])  # First element

# Slicing
print(arr[1:4])  # Elements from index 1 to 3

# Slicing 2D arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2, 1:])  # Slicing subarray



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
print(a + b)

# Subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
print(a / b)

# Dot product
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))




# -------------- universal function----------
arr = np.array([1, 2, 3, 4])

# Square root
print(np.sqrt(arr))

# Exponential
print(np.exp(arr))

# Sine
print(np.sin(arr))

# Logarithm
print(np.log(arr))


#-----------Aggregation function-------

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Sum
print(np.sum(arr))

# Sum along axis
print(np.sum(arr, axis=0))  # Sum of columns
print(np.sum(arr, axis=1))  # Sum of rows

# Mean
print(np.mean(arr))

# Median
print(np.median(arr))

# Standard deviation
print(np.std(arr))




#-------------Reshaping and Flattening Arrays--------------
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape
reshaped = arr.reshape((3, 2))
print(reshaped)

# Flatten
flattened = arr.flatten()
print(flattened)



#-----------------Stacking----------------
a = np.array([1, 2])
b = np.array([3, 4])

# Vertical stack
print(np.vstack((a, b)))

# Horizontal stack
print(np.hstack((a, b)))


#-------------------Splitting--------------
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Horizontal split
print(np.hsplit(arr, 3))

# Vertical split
print(np.vsplit(arr, 2))
