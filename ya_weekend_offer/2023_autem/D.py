import collections
import heapq


def solution():
    if len(plan) > m:
        return -1

    heap = []
    for key, val in plan.items():
        val.sort()
        greed = 0
        if len(val) > 1:
            greed = val[-1] - val[-2]

        heapq.heappush(heap, (-greed, key))

    # print(plan)
    # print(heap)

    step = m
    total_greed = 0
    while step:
        last_max = heapq.heappop(heap)
        # print(f'{last_max=}')
        greed, key = last_max
        # print(f'{greed=}, {key=}')

        total_greed += greed * -1
        if plan[key]:
            plan[key].pop()
            # print(f'{plan[key]=}')
            if plan[key]:
                cur_greed = 0 if len(plan[key]) == 1 else plan[key][-1] - plan[key][-2]
                heapq.heappush(heap, (-cur_greed, key))

        step -= 1

    return total_greed


if __name__ == "__main__":
    k, n, m = map(int, input().split())

    plan = collections.defaultdict(list)
    for _ in range(n):
        d, w = map(int, input().split())
        plan[w].append(d)

    print(solution())
