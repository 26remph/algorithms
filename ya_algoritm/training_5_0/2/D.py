def solution():
    di = (-1, 0, 1, 0)
    dj = (0, 1, 0, -1)

    ans = 0
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            if arr[i][j] == 0:
                for k in range(4):
                    val = arr[i + di[k]][j + dj[k]]
                    # print(f'{i=}, {j=}, {val=}, {(i + di[k])=}, {(j + dj[k])=}, {k=}')
                    if val > 0:
                        ans += val
            else:
                for k in range(4):
                    val = arr[i + di[k]][j + dj[k]]
                    if val == -1:
                        ans += arr[i][j]
    return ans


if __name__ == '__main__':
    N = int(input())
    M = 8
    arr = [
        [-1 if i == 0 or i == M + 1 or j == 0 or j == M + 1 else 0 for j in range(M + 2)] for i in range(M + 2)
    ]
    for _ in range(N):
        i, j = map(int, input().split())
        arr[i][j] = 1

    print(solution())
    # for row in arr:
    #     print(row)
