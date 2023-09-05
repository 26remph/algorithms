N, M = int(input()), int(input())
ans = set()
for _ in range(N + M):
    s = input()
    if s in ans:
        ans.remove(s)
    else:
        ans.add(s)

print('\n'.join(sorted(list(ans))) if ans else 'Таких нет')
