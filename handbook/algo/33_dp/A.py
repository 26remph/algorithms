n, m = map(int, input().split())
dp = [[-1 for _ in range(max(3, m + 1))] for _ in range(max(3, n + 1))]

dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 1
dp[2][0] = 0
dp[0][2] = 0


for i in range(n + 1):
    for j in range(m + 1):
        if dp[i][j] != -1 or (not i and not j):
            continue

        if not i:
            dp[i][j] = 1 if dp[i][j - 1] == 0 else 0

        if not j:
            dp[i][j] = 1 if dp[i - 1][j] == 0 else 0

        if i > 0 and j > 0:
            dp[i][j] = (
                0
                if all([dp[i - 1][j] == 1, dp[i][j - 1] == 1, dp[i - 1][j - 1] == 1])
                else 1
            )

# for i in range(n+1):
#     print(dp[i])

print("Win" if dp[n][m] else "Loose")
