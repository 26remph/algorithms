from collections import defaultdict


N = int(input())
stat = defaultdict(list)
for _ in range(N):
    f, *eat = input().split()
    for e in eat:
        stat[e].append(f)
q = input()
ans = stat.get(q)
if ans:
    ans.sort()
    print('\n'.join(ans))
else:
    print('Таких нет')
