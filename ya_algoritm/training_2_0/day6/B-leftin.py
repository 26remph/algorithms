from bisect import bisect_left, bisect_right
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
Q = list(map(int, input().split()))


def bi_left(a, x):
    i = bisect_left(a, x)
    return i + 1 if i != len(a) and a[i] == x else 0


def bi_right(a, x):
    i = bisect_right(a, x)
    return i if a[i-1] == x else 0


for q in Q:
    l, r = bi_left(arr, q), bi_right(arr, q)
    print(l, r)
