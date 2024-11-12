import numpy as np


# slice example
a = np.arange(1, 13).reshape(3, 4)
print(a)
print()
print(a[:2, 2:])
print()
print(a[:, ::2])

# circle
for row in a:
    print("row:", row)
