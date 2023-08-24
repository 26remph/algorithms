def solution(arr):

    ans = 0
    cur = 0
    for i in range(len(arr)):
        cur += arr[i]
        if cur < 0:
            cur = 0
        ans = max(ans, cur)

    print(ans)


if __name__ == '__main__':
    arr = [1, 6, -5, -4, 3, 8, -1, 3]
    solution(arr)