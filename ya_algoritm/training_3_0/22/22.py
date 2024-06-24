n, k = map(int, input().split(' '))

f0, f1 = 1, 1
dp = [f0, f1]

if k == 1:
    print(k)
elif n < 2:
    print(dp[0])
else:
    if n < k:
        k = n

    for i in range(2, n):
        lind = max(i - k, 0)
        dp.append(sum(dp[lind:i]))

    print(dp[-1])
