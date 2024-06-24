
def check(mid, a, s1, b, s2):

    if a < b:
        return (b + mid * s2) - (a + mid * s1) <= delta

    return (a + mid * s1) - (b + mid * s2) <= delta


def bin_answer(t1, t2, x1, v1, x2, v2):
    while abs(t1 - t2) / max(1, t2) >= delta:
        mid = (t1 + t2) / 2
        if check(mid, x1, v1, x2, v2):
            t2 = mid
        else:
            t1 = mid + delta
    return t1


def shift_iniit_pos(L, x1, v1, x2, v2):

    shift_x1_to_zero = x1 / abs(v1) if v1 != 0 else 0
    shift_x1_to_l2 = (L / 2 - x1) / abs(v1) if v1 != 0 else 0
    shift_x2_to_zero = x2 / abs(v2) if v2 != 0 else 0
    shift_x2_to_l2 = (L / 2 - x2) / abs(v2) if v2 != 0 else 0

    shift = 0
    if x1 < x2:
        if v1 == 0 and v2 > 0:
            shift = shift_x2_to_l2
            x2 += shift * abs(v2)
            v2 = -v2
        if v2 == 0 and v1 < 0:
            shift = shift_x1_to_zero
            x1 -= shift * abs(v1)
            v1 = -v1
        if v1 < 0 and v2 > 0:
            shift = min(shift_x1_to_zero, shift_x2_to_l2)
            x1 -= shift * abs(v1)
            x2 += shift * abs(v2)
            if shift_x1_to_zero < shift_x2_to_l2:
                v1 = -v1
            elif shift_x1_to_zero > shift_x2_to_l2:
                v2 = -v2
            else:
                v1, v2 = -v1, -v2
    else:
        if v1 == 0 and v2 < 0:
            shift = shift_x2_to_zero
            x2 -= shift * abs(v2)
            v2 = -v2
        if v2 == 0 and v1 > 0:
            shift = shift_x1_to_l2
            x1 += shift * abs(v1)
            v1 = -v1
        if v1 > 0 and v2 < 0:
            shift = min(shift_x2_to_zero, shift_x1_to_l2)
            x1 += shift * abs(v1)
            x2 -= shift * abs(v2)
            if shift_x1_to_l2 < shift_x2_to_zero:
                v1 = -v1
            elif shift_x1_to_l2 > shift_x2_to_zero:
                v2 = -v2
            else:
                v1, v2 = -v1, -v2

    return x1, v1, x2, v2, shift


def shift_pos(L, x1, v1, x2, v2):
    shift = 0
    if x1 < x2 and v1 < 0 and v2 < 0:
        shift = x1 / abs(v1)
        x2 -= abs(v2) * shift
        x1 = 0
        v1 = abs(v1)
    elif x1 < x2 and v1 > 0 and v2 > 0:
        shift = (L / 2 - x2) / abs(v2)
        x1 += abs(v1) * shift
        x2 = L / 2
        v2 = -abs(v2)
    elif x2 < x1 and v1 > 0 and v2 > 0:
        shift = (L / 2 - x1) / abs(v1)
        x2 += abs(v2) * shift
        x1 = L / 2
        v1 = -abs(v1)
    elif x2 < x1 and v1 < 0 and v2 < 0:
        shift = x2 / abs(v2)
        x1 -= abs(v1) * shift
        x2 = 0
        v2 = abs(v2)

    return x1, v1, x2, v2, shift


def main(L, x1, v1, x2, v2):

    ans = []
    # map to up coordinate square
    if x1 > L / 2:
        x1 = L - x1
        v1 = -v1
    if x2 > L / 2:
        x2 = L - x2
        v2 = -v2

    # equal point
    if x1 == x2:
        return 0
    # both not move
    if v1 == v2 == 0:
        return 'NO'

    # init position
    if x1 == 0 and x2 == L / 2:
        v1, v2 = abs(v1), -abs(v2)
    elif x2 == 0 and x1 == L / 2:
        v1, v2 = -abs(v1), abs(v2)
    elif x2 == L / 2:
        v2 = -abs(v2)
    elif x2 == 0:
        v2 = abs(v2)
    elif x1 == L / 2:
        v1 = -abs(v1)
    elif x1 == 0:
        v1 = abs(v1)

    x1, v1, x2, v2, shift = shift_iniit_pos(L, x1, v1, x2, v2)
    ans.append(shift)

    # monotonic decrease
    v_min = min(abs(v1), abs(v2))
    high_lim = 2 * (L / v_min if v_min > 0 else L / max(abs(v1), abs(v2)))

    time_to_meet = bin_answer(0, high_lim, x1, v1, x2, v2)
    time_limit = high_lim
    if v1 <= 0 and v2 <= 0 or v1 >= 0 and v2 >= 0:
        if x1 < x2:
            if v1 > 0 and v2 > 0:
                time_limit = (L / 2 - x2) / abs(v2)
            elif v1 < 0 and v2 < 0:
                time_limit = x1 / abs(v1)
        else:
            if v1 > 0 and v2 > 0:
                time_limit = (L / 2 - x1) / abs(v1)
            elif v1 <= 0 and v2 < 0:
                time_limit = x2 / abs(v2)

    if time_to_meet <= time_limit:
        ans.append(time_to_meet)
    else:
        x1, v1, x2, v2, shift = shift_pos(L, x1, v1, x2, v2)
        ans.append(shift)
        time_to_meet = bin_answer(0, high_lim, x1, v1, x2, v2)
        ans.append(time_to_meet)

    return sum(ans)


if __name__ == '__main__':
    L, x1, v1, x2, v2 = map(int, input().split())
    delta: float = 1e-09
    res = main(L, x1, v1, x2, v2)
    print(f'YES \n{round(res, 10)}')
