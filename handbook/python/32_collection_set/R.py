from collections import defaultdict
from pprint import pprint

N = int(input())
points = defaultdict(int)
for _ in range(N):
    p1, p2 = input().split()
    key1, key2 = '0', '0'
    if len(p1) > 1:
        key1 = p1[:-1]

    if len(p2) > 1:
        key2 = p2[:-1]

    points[key1+key2] += 1

pprint(points)
print(max(points.values()))