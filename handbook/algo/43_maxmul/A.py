def maxmul(a):

    max_mul = [(a[0], 0), (a[1], 1)]

    for i in range(len(a)):
        if a[i] > max_mul[0][0]:
            max_mul[1][0], max_mul[0][0] = max_mul[0], (a[i], i)
        ...

    return max_mul[0][0] * max_mul[1][0]


if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(maxmul(arr))