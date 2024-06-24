import sys


sys.setrecursionlimit(100_000)


def dfs(v):
    visited[v] = 1
    for e in graph[v]:
        if visited[e] == -1:
            visited[v] += dfs(e)

    return visited[v]


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

# print(visited)
# print(graph)
dfs(1)
print(*visited[1:])
