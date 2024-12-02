import matplotlib.pyplot as plt
import pandas as pd


students = pd.read_csv("sample_ds.csv")

plt.hist(students["math score"], label="math test")
plt.xlabel("score")
plt.ylabel("number student")
plt.legend()
plt.show()
