import sys


def dfs(v, prev):

    visited[v][0] = 1  # grey is one
    visited[v][1].append(prev)

    for e, flag in enumerate(graph[v]):
        if not flag:
            continue

        if not visited[e][0]:
            dfs(e, v)
            visited[e][0] = 2  # black node is two
        else:
            if visited[v][0] == visited[e][0] == 1 and e != prev:
                # print('cycle detect:', v, '->', e, 'prev', prev)
                # print('head', e, '->', visited[e])
                cycle = []
                i = v
                while i != e:
                    # print(i, '->', visited[i])
                    cycle.append(i)
                    i = visited[i][1][0]

                cycle.append(e)
                if not ans:
                    ans.append(cycle)


n = int(input())
graph = [[] for _ in range(n + 1)]
sys.setrecursionlimit(max(1000, n * 2))
visited = [[0, []]for _ in range(n + 1)]
ans = []

for v in range(1, n + 1):
    e = list(map(int, input().split(' ')))
    graph[v].extend([0] + e)


for v in range(1, n + 1):
    if not visited[v][0]:
        dfs(v, 0)
        visited[v][0] = 2

if ans:
    print('YES')
    print(len(ans[0]))
    print(*ans[0])
else:
    print('NO')


# print('---')
# print('ans:', ans)
# print(graph)
# for v in range(1, len(graph)):
#     e = [i for i in range(1, n+1) if graph[v][i]]
#     print(f'{v}: {e}')
