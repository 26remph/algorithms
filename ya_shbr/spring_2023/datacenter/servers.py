import heapq


n, m, q = map(int, input().split())
disabled = [set() for _ in range(n + 1)]
reboots = [0] * (n + 1)

heap_min = [(0, i + 1) for i in range(n)]
heap_max = [(0, i + 1) for i in range(n)]

for _ in range(q):
    log = input().split()
    int_args = tuple(map(int, log[1:]))

    if log[0] == "DISABLE" and int_args[1] not in disabled[int_args[0]]:
        disabled[int_args[0]].add((int_args[1]))
    elif log[0] == "RESET":
        disabled[int_args[0]].clear()
        reboots[int_args[0]] += 1
        # continue

    if log[0] in ("DISABLE", "RESET"):
        rp = reboots[int_args[0]] * (m - len(disabled[int_args[0]]))
        heapq.heappush(heap_min, (rp, int_args[0]))
        heapq.heappush(heap_max, (-rp, int_args[0]))
        continue

    heap_cur = heap_min if log[0] == "GETMIN" else heap_max
    k = 1 if log[0] == "GETMIN" else -1

    while heap_cur[0][0] != k * reboots[heap_cur[0][1]] * (
        m - len(disabled[heap_cur[0][1]])
    ):
        old = heapq.heappop(heap_cur)

    print(heap_cur[0][1])
