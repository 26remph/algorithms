from bisect import bisect_left, bisect_right


def left_search(i, j, num):

    while i < j:

        mid = (i + j) // 2
        if arr[mid] >= num:
            j = mid
        else:
            i = mid + 1

    return i if arr[i] >= num else -1


def right_search(i, j, num):

    while i < j:
        mid = (i + j + 1) // 2
        if arr[mid] <= num:
            i = mid
        else:
            j = mid - 1

    return i if arr[i] <= num else -1


def bin_my(lo, hi , num):

    while lo < hi:

        mid = lo + (hi-lo+1) // 2

        if num < arr[mid]:
            hi = mid - 1
        else:
            lo = mid

    return lo


def bi_left(a, x):
    i = bisect_left(a, x)
    return i


def bi_right(a, x):
    i = bisect_right(a, x)
    return i


N = int(input())
arr = list(map(int, input().split()))
K = int(input())
arr.sort()
ans = []

for _ in range(K):
    L, R = map(int, input().split())
    l1 = bi_left(arr, L)
    r1 = bi_right(arr, R)
    ans.append(str(r1 - l1))

print(' '.join(ans))
