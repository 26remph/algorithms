cash = 1_000
day = int(input())
price = list(map(int, input().split()))

by = [price[0], cash / price[0], 0]  # [price, quantity, day_index]
profit = [0, 0, 0]  # [profit:int, day_by, day_sell]

for i in range(len(price)):
    if price[i] >= by[0]:
        if (price[i] - by[0]) * by[1] > profit[0]:
            profit[0] = (price[i] - by[0]) * by[1]
            profit[1], profit[2] = by[2], i
    else:
        by = [price[i], cash / price[i], i]

ans = [0, 0]
if profit[1] > 0 and profit[2] > 0:
    ans = [profit[1] + 1, profit[2] + 1]

print(" ".join(map(str, ans)))
