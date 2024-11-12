n, m = map(int, input().split())
# t = time.time()
dp = [[-1 for _ in range(max(4, m + 1))] for _ in range(max(4, n + 1))]
# print(time.time() - t, '(s)')

dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 0
dp[2][0] = 1
dp[0][2] = 1
dp[2][1] = 1
dp[1][2] = 1

for i in range(n + 1):
    for j in range(m + 1):
        if dp[i][j] != -1 or (not i and not j):
            continue

        if not i:
            dp[i][j] = 0 if dp[i][j - 1] and dp[i][j - 2] else 1

        if not j:
            dp[i][j] = 0 if dp[i - 1][j] and dp[i - 2][j] else 1

        if i > 0 and j > 0:
            if (
                dp[i - 1][j]
                and dp[i - 2][j]
                and dp[i - 1][j - 2]
                and dp[i][j - 1]
                and dp[i][j - 2]
                and dp[i - 2][j - 1]
            ):
                dp[i][j] = 0
            else:
                dp[i][j] = 1
            # dp[i][j] = 0 if all(choice) else 1

# for i in range(n+1):
#     print(dp[i])

print("Win" if dp[n][m] else "Loose")
# print(time.time() - t, '(s)')
