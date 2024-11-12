import itertools

from collections import defaultdict, deque


n = int(input())
m = int(input())

graph: list[list[list[tuple[int, int, int]]]]  # (vertex, line, cost)
graph = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
subway = defaultdict(set)

for line in range(1, m + 1):
    p = list(map(int, input().strip().split(" ")))
    for i in range(1, len(p) - 1):
        v, e = p[i], p[i + 1]
        graph[line][v].append((e, line, 0))
        graph[line][e].append((v, line, 0))
        subway[v].add(line)
        subway[e].add(line)

for v, lines in subway.items():
    if len(lines) > 1:
        for cross in itertools.combinations(lines, 2):
            point, end = cross
            graph[end][v].append((v, point, 1))
            graph[point][v].append((v, end, 1))

# DEBUG
# print('---')
# print('sub', subway)
# for line in range(m+1):
#     print('ln:', line)
#     for station in range(n+1):
#         print(f'{station}: {graph[line][station]}')

# forward
a, b = map(int, input().split(" "))
visited: list[list[None | int]]  # vertex, line
visited = [[None for _ in range(m + 1)] for _ in range(n + 1)]
for line in subway[a]:
    visited[a][line] = 0

path = deque()
for line in subway[a]:
    point = (a, line, 0)
    for e in graph[line][a]:
        if e[2] == 0:
            path.appendleft((point, e))
        else:
            path.append((point, e))

# print('---')
# print('path', path)
# print('v:', visited)

success = False
out_st = (0, 0)
while path:
    v, e = path.popleft()
    if visited[e[0]][e[1]] is None:
        visited[e[0]][e[1]] = visited[v[0]][v[1]] + e[2]
        if e[0] == b:
            success = True
            out_st = (e[0], e[1])
            break
        for neig in graph[e[1]][e[0]]:
            if neig[2] == 0:
                path.appendleft((e, neig))
            else:
                path.append((e, neig))

# print('---')
# print(out_st)
# print('v:', visited)
# print(visited[5][2], out_st[1], out_st[0])
if a == b:
    print(0)
else:
    print(visited[out_st[0]][out_st[1]] if success else -1)
