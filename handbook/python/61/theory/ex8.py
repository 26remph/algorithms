import numpy as np


# Matrix operation
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

print(np.dot(a, b))
print(a @ b)

# min, max, sum
print(a.sum())
print(a.min())
print(a.max())
