N = int(input())

kitchen = set()
for _ in range(N):
    kitchen.add(input())

complete = set()
M = int(input())
for _ in range(M):
    col = int(input())
    for _ in range(col):
        complete.add(input())

ans = list(kitchen - complete)
ans.sort()
if ans:
    print('\n'.join(ans))
else:
    print('Готовить нечего')
