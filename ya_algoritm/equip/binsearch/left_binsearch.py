def check(m, params):
    return True


def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1

    return l
