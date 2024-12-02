import pandas as pd


# dictionary set
d = {"a": 10, "b": 20, "c": 30, "g": 40}
print(pd.Series(d))
print()
print(pd.Series(d, index=["a", "b", "c", "d"]))

# number sets
index = ["a", "b", "c"]
print(pd.Series(5, index=index))
