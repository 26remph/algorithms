def solution(n, m):

    frmt = str(len(str(n * m))) + 'd'
    arr = []
    for i in range(n):

        r = range(m * i + 1, m * i + m + 1)
        if i % 2 != 0:
            r = range(m * i + m, m * i, -1)

        for j in r:
            arr.append(f'{j:{frmt}}')

        print(' '.join(arr))
        arr = []


if __name__ == '__main__':
    n, m = int(input()), int(input())
    solution(n, m)