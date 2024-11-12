a, b, c, d = map(int, input().split())

EPS = 0.00001


def bi_left(lo, hi):
    while lo + EPS < hi:
        x = (hi + lo) / 2

        if a > 0:
            check = (a * pow(x, 3) + b * pow(x, 2) + c * x + d) >= 0
        else:
            check = (a * pow(x, 3) + b * pow(x, 2) + c * x + d) <= 0

        if check:
            hi = x
        else:
            lo = x

    return lo


ans = bi_left(-10000, 10000) + EPS if a > 0 else bi_left(-10000, 10000)

print(ans)
