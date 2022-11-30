A, K, B, M, X = map(int, input().split())


def bin_left(lo, hi):

    while lo < hi:

        day = (lo + hi) // 2

        progress_one = A * (day - day // K)
        progress_two = B * (day - day // M)
        total = progress_one + progress_two

        if total >= X:
            hi = day
        else:
            lo = day + 1

    return lo


print(bin_left(0, pow(10, 18)))

