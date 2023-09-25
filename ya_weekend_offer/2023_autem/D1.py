import collections


def solution():

    if len(plan) < m:
        return -1

    if len(plan) == m:
        greed = 0
        for key, val in plan.items():
            greed += max(val) - min(val)
        return greed
    else:
        return 4 / 0


if __name__ == '__main__':
    k, n, m = map(int, input().split())
    plan = collections.defaultdict(list)
    for _ in range(n):
        d, w = map(int, input().split())
        plan[w].append(d)

    print(solution())