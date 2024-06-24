from collections import defaultdict


N = int(input())
toys = defaultdict(int)
for _ in range(N):
    s = input()
    name = s[:s.index(':')]
    child_toys = set(s[s.index(':') + 1:].strip().split(', '))
    for t in child_toys:
        toys[t] += 1

# print(toys)
ans = []
for key, val in toys.items():
    if val == 1:
        ans.append(key)

ans.sort()
print('\n'.join(ans))
