from collections import defaultdict
from pprint import pprint

L, N, M = map(int, input().split())

pref = [0] * (L + 1)

cuts = defaultdict(list)
for i in range(N):
    l, r = map(int, input().split())
    cuts[l].append((l, 1, i))
    cuts[r].append((r, -1, i))

pprint(cuts)

for i in range(1, len(pref)):
    points = cuts.get(i)
    thin = 0
    if points:
        thin = sum([1 for p in points if p[1] < 0])

    pref[i] = pref[i-1] + thin

print('pref:', pref)
for _ in range(M):
    m = int(input())
    print(pref[m])

