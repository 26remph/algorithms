import sys

from collections import deque


def get_num(z, x, y) -> None | int:
    num = None
    if 0 < x <= n and 0 < y <= n and 0 < z <= n:
        shift = (z - 1) * n * n
        num = ((x - 1) * n + y) + shift

    return num


def get_neig(dot, plan) -> list[tuple[int, int, int]]:
    z, x, y = dot
    edges = [
        (z, x + 1, y), (z, x - 1, y),
        (z, x, y + 1), (z, x, y - 1),
        (z + 1, x, y), (z - 1, x, y)
    ]

    neig = []
    for dot in edges:
        num = get_num(dot[0], dot[1], dot[2])
        if num and plan[dot[0]][dot[1]][dot[2]] == '.':
            neig.append(dot)

    return neig


n = int(input())
out_dot = set()
enter_dot = (0, 0, 0)
z, i = 0, 0
cave = [[[None for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
while row := sys.stdin.readline():

    s = row.rstrip()
    if s:
        for j in range(1, n + 1):
            cave[z][i][j] = s[j - 1]
            if s[j - 1] == 'S':
                enter_dot = (z, i, j)
            if z == 1 and (s[j - 1] == '.' or s[j - 1] == 'S'):
                out_dot.add((z, i, j))
        i += 1
    else:
        z += 1
        i = 1

# print cave array
# for z in range(n+1):
#     print('z:', z)
#     for i in range(n+1):
#         print(f'{i}: {cave[z][i]}')
# print('e_dot', enter_dot)
# print('out_dor', out_dot)

# init visited
visited: list[None | int] = [None for _ in range(pow(n, 3) + 1)]
ind = get_num(enter_dot[0], enter_dot[1], enter_dot[2])
# for z in range(n+1):
#     for i in range(n+1):
#         for j in range(n+1):
#             print('dot:', (z, i, j), '->', get_num(z, i, j))

visited[ind] = 0
path = deque()  # init deq
if enter_dot not in out_dot:
    for neig in get_neig(enter_dot, cave):
        path.append((enter_dot, neig))
    away_dot = (0, 0, 0)
else:
    away_dot = enter_dot

while path:
    v, e = path.popleft()
    ind_v, ind_e = get_num(v[0], v[1], v[2]), get_num(e[0], e[1], e[2])

    if visited[ind_e] is None:
        visited[ind_e] = visited[ind_v] + 1
        if e in out_dot:
            away_dot = e
            # print('sucsess ind', ind_e, e)
            # print('path', path)
            break
        for neig in get_neig(e, cave):
            path.append((e, neig))


# print(visited)
ind = get_num(away_dot[0], away_dot[1], away_dot[2])
# print('exit:', away_dot, 'ind', ind)
print(visited[ind])
