import itertools


n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
for g1, g2 in itertools.combinations(lst, 2):
    print(g1, "-", g2)
