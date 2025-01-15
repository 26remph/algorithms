import math


n, m = map(int, input().split())
v1 = math.comb(n, m)
v2 = math.comb(n - 1, m - 1)
print(v2, v1)
