
def can_locate(lengh) -> bool:

    cnt = 1
    last_ind = 0
    for i in range(1, N):
        if arr[i] - arr[last_ind] >= lengh:
            cnt += 1
            last_ind = i

    return True if cnt >= K else False


def bin_search(lo, hi):

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_locate(mid):
            lo = mid
        else:
            hi = mid - 1

    return lo


N, K = map(int, input().split())
arr = list(map(int, input().strip().split(' ')))
ans = 0
if K > 1:
    ans = bin_search(1, max(arr) + 1)
print(ans)


# while True:
#
#     N = random.randint(2, 10_001)
#     K = random.randint(1, N)
#     arr = [random.randint(1, 1_000_000_000) for x in range(0, N)]
#     arr.sort()
#     print('N:', N, 'K:', K)
#     print('arr:', arr)
#
#     ans = 0
#     if K > 1:
#         ans = bin_search(1, max(arr) + 1)
#     print(ans)
