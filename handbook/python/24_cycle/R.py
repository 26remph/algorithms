def solution(n):

    cnt = 1
    arr = []
    max_width = 1
    for i in range(1, n + 1):

        if cnt > len(arr):
            arr.append(i)
        else:
            max_width = max(max_width, len(' '.join(map(str, arr))))
            arr = [i]
            cnt += 1

    max_width = max(max_width, len(' '.join(map(str, arr))))

    cnt = 1
    arr = []
    for i in range(1, n + 1):
        if cnt > len(arr):
            arr.append(i)
        else:
            res = ' '.join(map(str, arr))
            print(f'{res:^{max_width}}')
            arr = [i]
            cnt += 1

    res = ' '.join(map(str, arr))
    print(f'{res:^{max_width}}')


if __name__ == '__main__':
    N = int(input())
    solution(N)