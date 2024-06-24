n = int(input())
f0, f1, f2 = 1, 2, 4

if n == 0:
    print(f0)
elif n == 1:
    print(f1)
elif n == 2:
    print(f2)
else:
    dp = [f0, f1, f2]
    for i in range(2, n):
        dp.append(dp[i - 2] + dp[i - 1] + dp[i])

    print(dp[n])
