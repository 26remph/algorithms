from itertools import islice, repeat

m = int(input())
eats = []
for _ in range(m):
    eats.append(input())
n = int(input())

k = n // m + 1
for e in islice(eats * k, n):
    print(e)

