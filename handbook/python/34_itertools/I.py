from itertools import product
from math import prod


n = int(input())
cnt = 0
for x in product(range(1, n + 1), repeat=2):
    if cnt < n - 1:
        print(prod(x), end=" ")
        cnt += 1
    else:
        print(prod((x)))
        cnt = 0
