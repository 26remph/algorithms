import collections
import sys

sys.setrecursionlimit(2_000)


def dfs(v, level):
    visited[v] = True
    if graph[v]:
        for i in graph[v]:
            if not visited[i]:
                level += 1
                if max_repo[0] < level:
                    max_repo[0], max_repo[1] = level, i
                dfs(i, level)
                level -= 1


if __name__ == '__main__':
    n = int(input())
    graph = collections.defaultdict(list)
    for i in range(1, n + 1):
        h = int(input())
        graph[h].append(i)
    max_repo = [0, 0]  # level, n
    visited = [False] * (n + 1)
    dfs(0, 1)
    print(max_repo[1])
