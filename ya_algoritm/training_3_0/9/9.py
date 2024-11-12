n, m, k = map(int, input().split(" "))

arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

cnt = 0
for i in range(1, n + 1):
    m = list(map(int, input().strip().split(" ")))

    if i == 1:
        cnt = m[0]
        for j in range(len(m)):
            arr[i][j + 1] = arr[i][j] + m[j]

    else:
        for j in range(len(m)):
            if j == 0:
                arr[i][j + 1] = cnt + m[j]
                cnt = arr[i][j + 1]
            else:
                arr[i][j + 1] = arr[i - 1][j + 1] + arr[i][j] + m[j] - arr[i - 1][j]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split(" "))
    ans = arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1]
    print(ans)


# print(arr)
# for i in range(len(arr)):
#     print(f'{i}:{arr[i]}')
