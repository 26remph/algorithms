import numpy as np


# Error out of bounds for uint8
a = np.array([1, 2, 3], dtype="uint8")
a[0] = 256
print(a)
