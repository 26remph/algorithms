from collections import deque

getv = lambda i, j: (i-1) * m + j if 0 < i <= n and 0 < j <= m else None


def get_neig(dot) -> list[tuple[int, int]]:
    x, y = dot
    edge = [
        (x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
        (x-1, y-2), (x+1, y-2), (x-1, y+2), (x+1, y+2)
    ]
    return [(dot[0], dot[1]) for dot in edge if getv(dot[0], dot[1])]


n, m, s, t, q = map(int, input().strip().split(' '))

OUT = (s, t)
L, prev = None, None
arr: list[list[None | int | bool]]
arr = [[L, prev] for _ in range(n * m + 1)]


# init deq
path = deque()
ind_v = getv(OUT[0], OUT[1])
arr[ind_v][0] = 0
for neig in get_neig(OUT):
    path.append((OUT, neig))

while path:
    v, e = path.popleft()
    ind_v, ind_e = getv(v[0], v[1]), getv(e[0], e[1])

    if arr[ind_e][0] is None:
        arr[ind_e][0] = arr[ind_v][0] + 1
        arr[ind_e][1] = ind_v
        for neig in get_neig(e):
            path.append((e, neig))

# DEBUG
# i, j = 4, 1
# ind = getv(i, j)
# path = [ind]
# while arr[ind][1] is not None:
#     path.append(arr[ind][1])
#     ind = arr[ind][1]
# print(path)
# print(arr)


total_len = 0
for _ in range(q):
    i, j = map(int, input().strip().split(' '))
    cur_len = arr[getv(i, j)][0]
    if cur_len is None:
        total_len = -1
        break
    total_len += cur_len

print(total_len)