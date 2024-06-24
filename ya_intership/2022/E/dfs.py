# Смежность вершин
import random
import time

from collections import deque


# inc = {
#     1: {2, 8},
#     2: {1, 3, 8},
#     3: {2, 4, 8},
#     4: {3, 7, 9},
#     5: {6, 7},
#     6: {5},
#     7: {4, 5, 8},
#     8: {1, 2, 3, 7},
#     9: {4},
# }

inc = {
    3: {5},
    4: {3},
    5: set(),
    6: {3, 4, 5},
    7: {5},
    8: {3, 5},
    9: {10},
    10: {9},
    11: {13},
    12: {11},
    13: {12},
}


N = 10000


def gen_graph():
    inc = {}
    rnd = lambda _: random.randint(3, N)
    for i in range(3, N + 1):
        inc[i] = {rnd(1) for _ in range(5)}

    return inc


inc = gen_graph()
# pprint(inc)

start_time = time.time()

# start = 3
for start in range(3, N + 1):
    node_to_visit = deque()
    node_to_visit.append(start)
    loop_point = []
    loop_detect = False

    while node_to_visit:
        x = node_to_visit.popleft()
        cur_node = inc[x]
        for node in cur_node:
            # print('node', node)
            rib = (node, x)
            if rib in loop_point and node:
                # print(f'loop detect: from {x} to {node}')
                # print(f'loop point: {loop_point}')
                loop_detect = True
                break
            loop_point.append((node, x))
            node_to_visit.append(node)

        if loop_detect:
            break

# print('node_to_visit:', node_to_visit)
# print('loop_point:', loop_point)
print('total time:', time.time() - start_time, 'sec.')


# visited = set()  # Посещена ли вершина?
# Q = []  # Очередь
# BFS = []


# Поиск в ширину - ПВШ (Breadth First Search - BFS)
# def bfs(v):
#     if v in visited:  # Если вершина уже посещена, выходим
#         return
#     visited.add(v)  # Посетили вершину v
#     BFS.append(v)  # Запоминаем порядок обхода
#     # print("v = %d" % v)
#     for i in inc[v]:  # Все смежные с v вершины
#         if not i in visited:
#             Q.append(i)
#     while Q:
#         bfs(Q.pop(0))
#
#
# start = 3
# bfs(start)  # start - начальная вершина обхода
# print(len(BFS))
# print(BFS)  # Выводится: [1, 2, 8, 3, 7, 4, 5, 9, 6]


# visited = set()
# def dfs(v):
#     if v in visited:
#         return
#     visited.add(v)
#     for i in inc[v]:
#         if i not in visited:
#             dfs(i)


# start = 3
# dfs(start)
# print(visited)
# print(len(visited))
