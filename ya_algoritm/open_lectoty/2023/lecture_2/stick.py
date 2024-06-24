from collections import defaultdict


s = input()
cnt = defaultdict(set, set())

for i in range(0, len(s), 2):
    cnt[s[i + 1]].add(s[i])

col = 0
for val in cnt.values():
    if len(val) == 3:
        col += 1

print(col)
