n = int(input())

inf = float("inf")
dp = [(0, inf, inf, inf), (0, inf, inf, inf), (0, inf, inf, inf)]
for i in range(3, n + 3):
    ti = tuple(map(int, input().strip().split(" ")))
    t = min(
        dp[i - 1][0] + ti[0], dp[i - 2][0] + dp[i - 1][2], dp[i - 3][0] + dp[i - 2][3]
    )
    dp.append((t, ti[0], ti[1], ti[2]))

print(dp[-1][0])
