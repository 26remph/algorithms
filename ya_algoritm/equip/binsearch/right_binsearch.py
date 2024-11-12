def check():
    return True


def rbinsearch(l, r, check, params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, params):
            l = m
        else:
            r = m - 1

    return l
