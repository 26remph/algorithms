def solution(vector):

    cnt = 0
    max_cnt = 0
    for i in range(len(vector)):
        if vector[i] == 1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0

    return max_cnt


if __name__ == '__main__':
    tests = [
        ((1, 1, 0, 1, 0), 2),
        ((1, 1, 0, 1, 1, 1), 3),
        ((1, 1, 1, 1, 1), 5),
        ((0, 0, 0), 0),
        ((), 0)
    ]

    for arr, ans in tests:
        assert solution(list(arr)) == ans, f'sol: {solution(list(arr))} != ans: {ans}'
