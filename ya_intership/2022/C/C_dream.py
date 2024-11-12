# https://lisiynos.github.io/s1/graph_alg_py.html

# # Смежность вершин
# inc = {
#     1: [2, 3],
#     2: [4, 5],
#     3: [6, 7],
#     4: [8, 9],
#     5: [10],
#     6: [],
#     7: [],
#     8: [],
#     9: [],
#     10: [],
# }

row = list(map(int, input().split()))
N, V = row[0], row[1]
arr = list(map(int, input().split()))

graph = {1: []}
route = {}
for v in range(1, N + 1):
    x = []
    left = (2 * v) if (2 * v <= N) else None
    right = (2 * v + 1) if (2 * v + 1) <= N else None

    p = None if v == 1 else route[v]

    route[left] = v
    route[right] = v
    x.extend((left, right, p))

    graph[v] = x

start = 1
for v in arr:
    vl = graph[v][0]
    vr = graph[v][1]
    p = graph[v][2]
    pp = None
    if p:
        pp = graph[p][2]

        if pp:
            if p == graph[pp][0]:
                graph[pp][0] = v
            else:
                graph[pp][1] = v
        else:
            start = v

        if v == graph[p][0]:
            graph[v][0] = p
            graph[p][0] = vl
            if vl:
                graph[vl][2] = p
        else:
            graph[v][1] = p
            graph[p][1] = vr
            if vr:
                graph[vr][2] = p

        graph[v][2] = pp
        graph[p][2] = v


def dfs(v):
    if v:
        dfs(graph.get(v)[0])
        if v != start:
            print(v)
        dfs(graph.get(v)[1])


print(start)
dfs(start)
