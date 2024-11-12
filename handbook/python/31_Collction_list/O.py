from collections import deque


def gcd_multi(numbs):
    if len(numbs) == 1:
        return numbs[0]
    elif not numbs:
        return

    deq = deque(sorted(numbs, reverse=True))
    while deq[1] > 0:
        while not (b := deq.pop()):
            pass

        deq = deque(map(lambda x: x % b, deq))
        deq.appendleft(b)

    return deq[0]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(gcd_multi(arr))
