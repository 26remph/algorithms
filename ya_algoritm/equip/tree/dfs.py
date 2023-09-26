def dfs(v, param):

    visited[v] = param  # mark as need
    for e in graph[v]:
        if not visited[e]:
            dfs(e, param)


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n + 1)]  # list adjacency
    visited = [0] * (n + 1)
    ...  # fill graph
    comp = 0  # component connectivity
    for i in range(n + 1):
        if not visited[i]:
            dfs(i, comp)
            comp += 1
