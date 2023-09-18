def maxmul(a):

    max_mul = [max((a[0], 0), (a[1], 1)), min((a[0], 0), (a[1], 1))]

    for i in range(len(a)):
        if a[i] > max_mul[0][0]:
            max_mul[1], max_mul[0] = max_mul[0], (a[i], i)
        elif a[i] > max_mul[1][0] and i != max_mul[0][1]:
            max_mul[1] = a[i], i

    # print(max_mul)
    return max_mul[0][0] * max_mul[1][0]


if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(maxmul(arr))

    tests = (
        ([2, 2], 4),
        ([1, 3], 3),
        ([3, 1], 3),
        ([3, 1, 3], 9),
        ([3, 1, 0], 3),
        ([1, 0, 3], 3),
        ([1, 2, 3], 6),
        ([0, 1], 0)
    )
    for lst, res in tests:
        ans = maxmul(lst)
        assert res == ans, f'{res=}, {ans=}'
