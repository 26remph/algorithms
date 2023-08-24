def solution(vector):

    z_cnt = 0
    total = 0
    left_summ = 0
    _max = 0
    for ch in vector:

        if ch == '1':
            if z_cnt < 1:
                left_summ += 1
            total += 1
        else:
            z_cnt += 1

            if z_cnt > 1:
                left_summ = total - left_summ
                _max = max(total, _max)
                z_cnt = 1
                total = left_summ

    _max = max(total, _max)

    return _max


if __name__ == '__main__':
    tests = (
        ('1110111011111', 8),
        ('10101', 2),
        ('101', 2),
        ('111', 3),
        ('000', 0)
    )

    for v, ans in tests:
        res = solution(v)
        assert res == ans, f'{v=}, {ans=}, {res=}'