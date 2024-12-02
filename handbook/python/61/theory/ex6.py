import numpy as np


a = np.zeros((4, 3), dtype="uint8")
print(a)
print()
a = a.reshape((2, 6))
print(a)
a = a.reshape((1, 12))
print(a)

print("-- auto reshape --")
a = a.reshape((-1, 6))
print(a)
