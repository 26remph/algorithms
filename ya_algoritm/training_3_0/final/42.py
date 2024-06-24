from collections import deque


def get_num(x, y) -> None | int:
    num = None
    if 0 < x <= n and 0 < y <= m:
        num = ((x - 1) * n + y)

    return num


def get_neig(dot, plan) -> list[tuple[int, int]]:
    x, y = dot
    edges = [(x - 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1)]

    neig = []
    for dot in edges:
        num = get_num(dot[0], dot[1])
        if num and plan[dot[0]][dot[1]] == '.':
            neig.append(dot)

    return neig


n, m = map(int, input().split(' '))
cave = [[None for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    s = input()
    for j in range(1, m + 1):
        cave[i][j] = s[j - 1]

i, j = map(int, input().split(' '))
enter_dot = (i, j)
i, j = map(int, input().split(' '))
out_dot = set()
out_dot.add((i, j))


# init visited
visited: list[list[None | int]] = [[None, None] for _ in range((n * m) + 1)]
ind = get_num(enter_dot[0], enter_dot[1])
visited[ind][0] = 1
visited[ind][1] = enter_dot
path = deque()  # init deq
if enter_dot not in out_dot:
    for neig in get_neig(enter_dot, cave):
        path.append((enter_dot, neig))
    away_dot = (0, 0)
else:
    away_dot = enter_dot


while path:
    v, e = path.popleft()
    ind_v, ind_e = get_num(v[0], v[1]), get_num(e[0], e[1])

    if visited[ind_e][0] is None:
        visited[ind_e][0] = visited[ind_v][0] + 1
        visited[ind_e][1] = v
        print(e, out_dot)
        if e in out_dot:
            away_dot = e
            break
        for neig in get_neig(e, cave):
            ind_e = get_num(e[0], e[1])
            prev_i, prev_j = visited[ind_e][1]
            if prev_i == neig[0] or prev_j == neig[1]:
                path.appendleft((e, neig))
            else:
                path.append((e, neig))

print()
ind = get_num(away_dot[0], away_dot[1])
print(visited[ind][0])
