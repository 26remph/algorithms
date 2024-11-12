from itertools import product


n = int(input())
print("A Б В")
# ans = []
# for pair in product(range(1, n - 1), repeat=2):
#     if sum(pair) >= n:
#         continue
#     ans.append((pair[0], pair[1], n - pair[0] - pair[1]))
ans = [
    (p1, p2, n - p1 - p2)
    for p1, p2 in [p for p in product(range(1, n - 1), repeat=2) if sum(p) < n]
]
ans.sort(key=lambda x: (x[0], x[1]))
for x in ans:
    print(*x)
