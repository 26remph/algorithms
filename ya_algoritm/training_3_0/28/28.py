n, m = map(int, input().strip().split(" "))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        step1 = i - 2, j - 1
        step2 = i - 1, j - 2
        sum_step = dp[step1[0]][step1[1]] + dp[step2[0]][step2[1]]
        dp[i][j] += sum_step

print(dp[-1][-1])
# for i in range(n+1):
#     print(f'{i}: {dp[i]}')
