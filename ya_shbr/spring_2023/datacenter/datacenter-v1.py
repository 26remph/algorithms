import heapq


n, m, q = map(int, input().split())
N = [[0, set()] for _ in range(n + 1)]
M = m
min_heap = [(0, i + 1) for i in range(n)]
max_heap = [(0, i + 1) for i in range(n)]

for _ in range(q):
    func, *args = input().split()

    if func == 'DISABLE':
        i, j = int(args[0]), int(args[1])
        N[i][1].add(j)

    if func == 'RESET':
        i = int(args[0])
        N[i][0] += 1
        N[i][1] = set()

    if func in ('DISABLE', 'RESET'):
        r = N[i][0]
        a = M - len(N[i][1])
        ra = r * a  # r*a

        heapq.heappush(min_heap, (ra, i))
        heapq.heappush(max_heap, (-ra, i))
        continue

    if func == 'GETMIN':
        while min_heap[0][0] != N[min_heap[0][1]][0] * (M - len(N[min_heap[0][1]][1])):
            heapq.heappop(min_heap)
        print(min_heap[0][1])

    if func == 'GETMAX':
        while max_heap[0][0] != -1 * N[max_heap[0][1]][0] * (
                M - len(N[max_heap[0][1]][1])
        ):
            heapq.heappop(max_heap)

        print(max_heap[0][1])
