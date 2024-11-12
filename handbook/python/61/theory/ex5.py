import numpy as np


# fill One into main diagonal
a = np.eye(4, 4, dtype=float)
print(a)
print(a.dtype)

# fill range
b = np.arange(1, 5, 0.4)
print(b)

# fill line space
c = np.linspace(1, 5, 10)
print(c)
