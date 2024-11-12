import sys


def dfs(v, cnt):
    visited[v] = True
    comp[cnt].append(v)
    if graph[v]:
        for i in graph[v]:
            if not visited[i]:
                dfs(i, cnt)


n, m = map(int, input().split(" "))
graph: list[list[int]] = [[] for _ in range(n + 1)]
sys.setrecursionlimit(max(997, n * 2))

for _ in range(m):
    v, h = map(int, input().split(" "))
    graph[v].append(h)
    graph[h].append(v)

visited: list[None | int] = [None for _ in range(n + 1)]
comp = [[] for _ in range(n + 1)]
cnt = 0
for i in range(1, len(graph)):
    if not visited[i]:
        cnt += 1
        dfs(i, cnt)

print(cnt)
for i in range(len(comp)):
    if comp[i]:
        print(len(comp[i]))
        print(*comp[i])

# print('---' * 25)
# for i in range(len(graph)):
#     print(f'{i}:{graph[i]}')
#
# print(comp)
