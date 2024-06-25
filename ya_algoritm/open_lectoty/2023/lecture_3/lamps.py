n, k = map(int, input().split())
arr = []

maq_q = 0
for i in range(k):
    q = int(input())
    arr.append((i, q))
    maq_q += q

arr.sort(reverse=True, key=lambda x: x[1])
spec = []


def can_produce(ask) -> bool:

    # print('ask -> ', ask)
    if ask > arr[0][1]:
        return False

    spec.clear()
    cnt = 0
    for i in range(k):
        tail = arr[i][1]
        # print('tail:', tail)
        while tail >= ask and cnt < n:
            cnt += 1
            tail -= ask
            spec.append(str(arr[i][0] + 1))

        # print('i:', i, 'cnt', cnt, 'ask:', ask)
        if cnt == n:
            return True

    return False


def bin_search(lo, hi):
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_produce(mid):
            lo = mid
            # print('hi:', hi)
        else:
            hi = mid - 1
            # print('lo', lo)

    return lo


ans = bin_search(1, maq_q // n + 1)
if can_produce(ans):
    print(ans)
    print('\n'.join(spec))
else:
    print(0)
