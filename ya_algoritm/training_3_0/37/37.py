from collections import deque


n = int(input())

graph = [[] for _ in range(n + 1)]
visited: list[list[None | int]] = [[None, None] for i in range(n + 1)]


for v in range(1, n + 1):
    graph[v].extend([0] + [*map(int, input().strip().split(" "))])

start, end = map(int, input().split(" "))

path = deque()
for e in range(len(graph[start])):
    if graph[start][e]:
        path.append((start, e))

visited[start][0] = 0

while path:
    v, e = path.popleft()
    if visited[e][0] is None:
        visited[e][0] = visited[v][0] + 1
        visited[e][1] = v
        for neig in range(len(graph[e])):
            if graph[e][neig]:
                path.append((e, neig))


L = visited[end][0] if visited[end][0] is not None else -1
print(L)
if L > 0:
    i = end
    path = [end]
    while visited[i][1] is not None:
        path.append(visited[i][1])
        i = visited[i][1]
    print(*reversed(path))

# print(visited)
# for i in range(len(graph)):
#     print(f'{i}: {[ind for ind in range(len(graph[i])) if graph[i][ind]]}')
