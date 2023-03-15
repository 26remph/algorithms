n, m = map(int, input().strip().split(' '))

dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    row = list(map(int, input().strip().split(' ')))
    for j in range(1, m+1):
        dp[i][j] = row[j-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == j == 1:
            continue
        left = dp[i][j-1], (i, j-1)
        up = dp[i-1][j], (i-1, j)
        cost = max(left, up, key=lambda x: x[0])
        dp[i][j] += cost[0]

max_coast = dp[-1][-1]
print(max_coast)
# print(dp)
# init path
path = []
i, j = n, m
while not(i == j == 1):
    left = dp[i][j - 1], 'R', (i, j - 1)
    up = dp[i - 1][j], 'D', (i - 1, j)
    cost = max(left, up)
    i, j = cost[2][0], cost[2][1]
    path.append(cost[1])

print(*reversed(path))

# for i in range(n+1):
#     print(f'{i}: {dp[i]}')
