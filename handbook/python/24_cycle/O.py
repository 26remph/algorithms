def solution(n, m):

    frmt = str(len(str(n * m))) + 'd'

    cnt = 1
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):

        rng = range(n)
        if j % 2 != 0:
            rng = range(n - 1, -1, -1)

        for i in rng:
            arr[i][j] = f'{cnt:{frmt}}'
            cnt += 1

    for i in arr:
        print(' '.join(i))


if __name__ == '__main__':
    n, m = int(input()), int(input())
    solution(n, m)