import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"a[0] = {a[0]}")
print(f"b[0] = {b[0]}")

print("-- array info --")
print("dimension:", a.ndim)  # number of axis
print("shape:", a.shape)  # shape array
print("dtype:", a.dtype)  # object data type
print("item_size:", a.itemsize)  # byte size one element
print("size:", a.size)  # total array element
