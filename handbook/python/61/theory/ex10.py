import numpy as np


a = np.arange(1, 13).reshape(4, 3)
print(a)
a = a.flatten()
print(a)

a = [str(el) for el in a.flat]
print(a)
