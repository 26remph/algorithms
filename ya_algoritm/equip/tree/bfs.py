from collections import deque


def bfs(start, end):

    # init deque
    path = deque([(start, e) for e in range(len(graph[start]))])

    # processing deque
    while path:
        v, e = path.popleft()
        if not visited[e]:
            visited[e] = visited[v] + 1
            for i in range(len(graph[e])):
                path.append((e, i))

    return visited[end]


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    ...  # fill graph
    bfs(0, 100)
