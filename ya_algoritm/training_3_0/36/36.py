from collections import deque


n = int(input())

graph = [[] for _ in range(n + 1)]
visited: list[None | int] = [None] * (n + 1)

for v in range(1, n + 1):
    graph[v].extend([0] + [*map(int, input().strip().split(' '))])

start, end = map(int, input().split(' '))

path = deque()
for e in range(len(graph[start])):
    if graph[start][e]:
        path.append((start, e))
visited[start] = 0

while path:

    v, e = path.popleft()
    if visited[e] is None:
        visited[e] = visited[v] + 1
        for neig in range(len(graph[e])):
            if graph[e][neig]:
                path.append((e, neig))


print(visited[end] if visited[end] is not None else -1)

# print(visited)
# for i in range(len(graph)):
#     print(f'{i}: {[ind for ind in range(len(graph[i])) if graph[i][ind]]}')
