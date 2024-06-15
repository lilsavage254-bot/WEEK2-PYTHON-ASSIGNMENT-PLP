import numpy as np

# Create a numpy array

a = np.array([1, 2, 3, 4, 5])
print(a)

# Create a 2D numpy array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Create a 3D numpy array.
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2)

# Create a numpy array with zeros.
zeros = np.zeros((2, 3))
print(zeros)

# Create a numpy array with ones.
ones = np.ones((2, 3))
print(ones)

# Mathematical operations on numpy arrays.
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Transposing an array.
transpose = np.array([[1, 2, 3], [4, 5, 6]])
print(transpose.reshape(3, 2))

transpose2 = transpose.T
print(transpose2)

for x in np.nditer(transpose2) :
    print(x)

# Indexing and slicing numpy arrays.
# Indexing
index = np.array([1, 2, 3, 4, 5])
print(index[0])
print(index[-1])

# Slicing
print(index[1:])
print(index[:3])

# Reshaping numpy arrays.
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
reshape = arr2.reshape(3, 2)
print(reshape)

# Dot product of two numpy arrays.
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr3, arr4)
print(dot_product)

# Element-wise multiplication of two numpy arrays.
element_wise = arr3 * arr4
print(element_wise)

array5 = np.arange(0, 81, 9)
new_array = array5.reshape(3, 3)
print(new_array)




