import pandas as pd


lx, ly = map(int, input().split())
rx, ry = map(int, input().split())
# print(lx, ly, rx, ry)

df = pd.read_csv("data/data.csv")
df = df[(lx <= df["x"]) & (df["x"] <= rx) & (ry <= df["y"]) & (df["y"] <= ly)]
print(df)
