n = int(input())


dp = [0, 0]
prev = [0, 1]
ind = 0
cost, cost1, cost2, cos3 = 0, 0, 0, 0
inf = float("inf")
for i in range(2, n + 1):
    if i % 3 == 0:
        ind = i // 3
        cost3 = (dp[ind] + 1, ind)
    else:
        cost3 = (inf, ind)

    if i % 2 == 0:
        ind = i // 2
        cost2 = (dp[ind] + 1, ind)
    else:
        cost2 = (inf, ind)

    ind = i - 1
    cost1 = (dp[ind] + 1, ind)

    cost = min(cost1, cost2, cost3, key=lambda x: x[0])

    dp.append(cost[0])
    prev.append(cost[1])
    # print('dp', dp, 'cost', cost, 'i', i, 'ind', ind)
    # print('prev', prev,)


ans = []
ind = prev[-1]
if len(prev) - 1 != 1:
    ans.append(len(prev) - 1)
ans.append(ind)

while ind > 1:
    ans.append(prev[ind])
    ind = prev[ind]

print(dp[-1])
print(*reversed(ans))
