import sys

def dfs(v):

    visited[v] = 1  # grey

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = 2  # black
            ans.append(i)
        else:
            if visited[v] == visited[i] == 1:
                graph[0][0] = False
                # print('cycle:', v, '->', i)


n, m = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]
graph[0].append(True)  # non cycled graph
visited = [0] * (n+1)
sys.setrecursionlimit(max(997, n*2))
ans = []

for _ in range(m):
    v, h = map(int, input().split(' '))
    graph[v].append(h)

for v in range(1, n+1):
    if not visited[v]:
        dfs(v)
        visited[v] = 2
        ans.append(v)

if graph[0][0]:
    print(*reversed(ans))
else:
    print('-1')

# print('---')
# for i in range(n+1):
#     print(f'{i}: {graph[i]}')
#
# print('ans', ans)
# print('vis', visited)
