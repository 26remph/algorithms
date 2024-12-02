import numpy as np
import pandas as pd


s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])

# slice and summ
print("-- Slice variant --")
print(s["a"])
print(s[["a", "d"]])
print(s[1:])
print("-- Summ --")
print(s + s)

# Filter
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("-- Filter --")
print(s[s > 2])

# Name
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
s.name = "Rsi"
s.index.name = "Key point"
print(s)
