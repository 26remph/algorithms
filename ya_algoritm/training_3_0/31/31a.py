import sys


def dfs(v):
    visited[v] = True
    if graph[v]:
        for i in graph[v]:
            if not visited[i]:
                dfs(i)


n, m = map(int, input().strip().split(" "))
graph: list[list[int]] = [[] for _ in range(n + 1)]
for _ in range(m):
    v, h = map(int, input().strip().split(" "))
    graph[v].append(h)
    graph[h].append(v)


visited: list[None | int] = [None] * (n + 1)
sys.setrecursionlimit(max(1000, n * 2))
dfs(1)

ans = [i for i in range(len(visited)) if visited[i]]
print(len(ans))
print(*ans)
