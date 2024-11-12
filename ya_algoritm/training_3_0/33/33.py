import sys


def dfs(v, col):
    visited[v] = [col, False]

    for i in graph[v]:
        if not visited[i][0]:
            dfs(i, 3 - col)
        else:
            if visited[i][0] == visited[v][0]:
                graph[0][0] = False

            visited[i][1] = True  # check neig complete
            visited[v][1] = True  # check neig complete


n, m = map(int, input().split(" "))

graph = [[] for _ in range(n + 1)]
graph[0].append(True)  # bipartite
sys.setrecursionlimit(max(997, n * 2))
for _ in range(m):
    v, h = map(int, input().split(" "))
    graph[v].append(h)
    graph[h].append(v)


visited: list[list[int | bool]] = [[0, False] for _ in range(n + 1)]
color = 1
for i in range(1, len(graph)):
    if not visited[i][0]:
        dfs(i, color)

print("YES" if graph[0][0] else "NO")

# for i in range(len(graph)):
#     print(f'{i}: {graph[i]}')
#
# print(visited)
# print(visited[83])
# print(visited[9])
# print(visited[48])
# print(visited[32])
