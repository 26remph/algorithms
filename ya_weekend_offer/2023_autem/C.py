import collections
import sys


sys.setrecursionlimit(2_000)


def solution(graph):

    def dfs(v, lvl):
        visited[v] = True
        if graph[v]:
            for i in graph[v]:
                if not visited[i]:
                    lvl += 1
                    if max_elm[0] < lvl:
                        max_elm[0] = lvl
                        max_elm[1] = i
                    dfs(i, lvl)
                    lvl -= 1

    max_elm = [0, 0]
    visited = [False] * (n + 1)
    dfs(0, 1)
    return max_elm[1]
    # for node in visited:
    #     if not visited:
    #         dfs(node)


if __name__ == '__main__':
    n = int(input())
    graph = collections.defaultdict(list)
    for i in range(1, n + 1):
        h = int(input())
        graph[h].append(i)
    # print(graph)
    print(solution(graph))
