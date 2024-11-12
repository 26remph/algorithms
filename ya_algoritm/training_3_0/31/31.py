import sys


def dfs(v):
    visited[v] = True
    if graph[v]:
        for i in graph[v]:
            if not visited[i]:
                dfs(i)


with open("input.txt") as f:
    row = f.readline().rstrip()
    n, m = map(int, row.split(" "))
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    sys.setrecursionlimit(max(1000, n * 2))

    while row := f.readline().rstrip():
        v, h = map(int, row.strip().split(" "))
        graph[v].append(h)
        graph[h].append(v)

visited: list[None | int] = [None] * (n + 1)
dfs(1)
ans = [i for i in range(len(visited)) if visited[i]]
print(len(ans))
print(*ans)

# for i in range(len(graph)):
#     print(f'{i}:{graph[i]}')
