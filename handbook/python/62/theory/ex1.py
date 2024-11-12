import pandas as pd
import numpy as np
import matplotlib. pyplot as plt

# create pandas series
data = np.arange(5)
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(s)
print()
s = pd.Series(np.linspace(0, 1, 5))
print(s)

# visualize
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])
plt.show()
