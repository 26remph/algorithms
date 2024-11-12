import heapq


class DataCenter:
    def __init__(self, N, M):
        self.N = [[0, set()] for _ in range(n + 1)]
        self.M = M
        self.min_heap = [(0, i + 1) for i in range(N)]
        self.max_heap = [(0, i + 1) for i in range(N)]

    def _update_heap(self, i):
        r = self.N[i][0]
        a = self.M - len(self.N[i][1])
        ra = r * a  # r*a

        heapq.heappush(self.min_heap, (ra, i))
        heapq.heappush(self.max_heap, (-ra, i))

    def reset(self, i):
        i = int(i)
        self.N[i][0] += 1
        self.N[i][1] = set()
        # self._update_heap(i)

    def disable(self, i, j):
        i, j = int(i), int(j)
        self.N[i][1].add(j)
        self._update_heap(i)

    def getmin(self):
        while self.min_heap[0][0] != self.N[self.min_heap[0][1]][0] * (
            self.M - len(self.N[self.min_heap[0][1]][1])
        ):
            heapq.heappop(self.min_heap)

        return self.min_heap[0][1]

    def getmax(self):
        while self.max_heap[0][0] != -1 * self.N[self.max_heap[0][1]][0] * (
            self.M - len(self.N[self.max_heap[0][1]][1])
        ):
            heapq.heappop(self.max_heap)

        return self.max_heap[0][1]


n, m, q = map(int, input().split())
dc = DataCenter(n, m)


for _ in range(q):
    row, *args = input().split()
    func = getattr(dc, str(row).lower())
    res = func(*args)
    if res:
        print(res)
