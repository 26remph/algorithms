def solution(arr, N):
    high = [(arr[i], i) for i in range(N)]

    center = max(high, key=lambda x: x[0])
    left = high[: center[1]]
    left.sort()

    right = high[center[1] + 1 :]
    right.sort(key=lambda x: (-x[0], x[1]))
    high = left + [center] + right
    # print('high', high)

    cnt = 0
    level = center[0]
    j = center[1]
    i_right_h = high[j][1]
    for i in range(center[1], N - 1):
        if i == i_right_h:
            while j < len(high) and (i_right_h := high[j][1]) <= i:
                j += 1

            level = min(arr[i], arr[i_right_h])
            # print('lvl', level)
            # print('i_right_h', i_right_h, 'val', arr[i_right_h])
        else:
            if i_right_h - i > 0:
                cnt += level - arr[i]

    # print(cnt)

    # cnt = 0
    level = center[0]
    j = center[1]
    i_left_h = high[j][1]
    for i in range(center[1], -1, -1):
        if i == i_left_h:
            while j > 0 and i_left_h >= i:
                i_left_h = high[j][1]
                j -= 1

            level = min(arr[i], arr[i_left_h])
            # print('lvl', level)
            # print('i_left_h', i_left_h, 'val', arr[i_left_h])
        else:
            if i - i_left_h > 0:
                cnt += level - arr[i]

        # print('cnt:', cnt)

    # print(cnt)
    return cnt


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(arr, N))

    # tests = [
    #     (11, (2, 5, 2, 3, 6, 9, 3, 1, 3, 4, 6), 18),
    #     (9, (100, 3, 3, 3, 50, 3, 3, 3, 100), 632),
    #     (9, (3, 5, 8, 12, 20, 12, 8, 5, 3), 0),
    #     (13, (5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5), 18),
    #     (7, (3, 4, 5, 6, 5, 4, 3), 0),
    #     (5, (6, 8, 4, 5, 1), 1),
    #     (8, (4, 3, 6, 2, 4, 2, 2, 6), 15),
    #     (11, (5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5), 16),
    #     (13, (3, 2, 8, 7, 6, 5, 4, 8, 2, 8, 6, 7, 8), 20),
    #     (13, (3, 2, 8, 7, 6, 5, 4, 8, 2, 8, 6, 7, 8), 20),
    #     (27, (
    #     3, 2, 8, 7, 6, 5, 4, 8, 2, 8, 6, 7, 8, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1,
    #     3, 1, 9), 84),
    #     (27, (
    #     3, 2, 8, 7, 6, 5, 4, 8, 2, 8, 6, 7, 8, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1,
    #     3, 1, 9), 84),
    #     (27, (
    #     10, 2, 8, 7, 6, 5, 4, 8, 2, 8, 6, 7, 8, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1,
    #     3, 1, 10), 139),
    #     (10, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10), 0),
    #     (10, (10, 11, 11, 11, 11, 11, 11, 11, 11, 10), 0),
    #     (11, (10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10), 4),
    #     (11, (10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10), 4),
    #     (10, (10, 9, 8, 7, 6, 5, 4, 3, 2, 1), 0),
    #     (10, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0),
    #     (19, (10, 1, 9, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2, 1, 1), 36),
    # ]
    #
    # for N, arr, res in tests:
    #     arr = list(arr)
    #     assert solution(arr, N) == res
