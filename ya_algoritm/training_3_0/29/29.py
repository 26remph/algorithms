n = int(input())
price = [0]
for _ in range(n):
    price.append(int(input().strip()))


inf = float('inf')
dp = [[inf for _ in range(n + 2)] for _ in range(n + 1)]

# init base
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(n + 1):
        if price[i] > 100:
            left_min = dp[i - 1][j - 1] if j - 1 >= 0 else dp[i - 1][j]
            dp[i][j] = min(left_min + price[i], dp[i - 1][j + 1])
        else:
            dp[i][j] = min(dp[i - 1][j] + price[i], dp[i - 1][j + 1])

ans = dp[-1]
print(ans[0])
ans_ind = 0
for i in range(n + 2):
    if ans[i] != ans[0]:
        ans_ind = i - 1
        break

day = []
if n > 0:
    i = n
    j = ans_ind
    while i != 1:
        if dp[i][j] == dp[i - 1][j + 1]:
            day.append(i)
            j += 1
        elif j > 0 and price[i] > 100:
            j -= 1

        i -= 1

print(ans_ind, len(day))
print(*reversed(day))

# print('---')
# print(price)
# for i in range(n+1):
#     print(f'{i}: {dp[i]}')
