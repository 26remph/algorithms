n, k = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

arr.sort(reverse=True)
spec = []


def can_produce(ask) -> bool:

    # print('ask -> ', ask)
    if ask > arr[0]: return False

    spec.clear()
    cnt = 0
    for i in range(k):
        tail = arr[i]
        # print('tail:', tail)
        while tail >= ask:
            cnt += 1
            tail -= ask
        spec.append(str(i+1))

        # print('i:', i, 'cnt', cnt, 'ask:', ask)
        if cnt >= n: return True

    return False


def bin_search(lo, hi):
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_produce(mid):
            lo = mid
            print('hi:', hi)
        else:
            hi = mid - 1
            print('lo', lo)

    return lo


ans = bin_search(1, sum(arr) // n + 1)
if can_produce(ans):
    print(ans)
    print('\n'.join(spec))
else:
    print(0)
