import numpy as np


a = np.zeros((4, 3))
print(a)
print()
a = np.zeros((4, 3), dtype="int32")
print(a)

print("-- 3 axis --")
b = np.zeros((4, 3, 2), dtype="int32")
print(b)

print("-- 2 axis, fill ones --")
c = np.ones((4, 2), dtype="uint8")
print(c)
