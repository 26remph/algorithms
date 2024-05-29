def solution(n, m):

    frmt = str(len(str(n * m))) + 'd'
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
        for _ in range(1, m):
            arr.append(arr[-1] + n)

        arr = [f'{x:{frmt}}' for x in arr]
        print(' '.join(arr))
        arr = []


if __name__ == '__main__':
    n, m = int(input()), int(input())
    solution(n, m)