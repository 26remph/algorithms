
def true_solving(n, cost):
    minIndex = 0
    maxGas = 1 / cost[0]
    maxRevenue = 0
    ans = (0, 0)
    for i in range(1, n):
        if maxGas * cost[i] - 1 > maxRevenue:
            maxRevenue = maxGas * cost[i] - 1
            ans = (minIndex + 1, i + 1)
        if 1 / cost[i] > maxGas:
            minIndex = i
            maxGas = 1 / cost[i]
    return ans


def profit_day(_, data):

    CASH = 1000
    min_d = max_d = (1, data[0])
    profit = (min_d[0], max_d[0], 0)

    for day, price in enumerate(data):

        if price < min_d[1]:
            min_d = (day + 1, price)
            max_d = min_d
        elif price > max_d[1]:
            max_d = (day + 1, price)
            delta = (max_d[1] - min_d[1]) * (CASH / price)
            if profit[2] < delta:
                profit = (min_d[0], max_d[0], delta)

    if profit[2] == 0:
        return 0, 0
    else:
        return profit[0], profit[1]


n = int(input())
data = list(map(int, input().split()))
print(*profit_day(n, data))

data = [10, 3, 5, 4, 11, 9]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [10, 3, 5, 3, 11, 9]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [5, 5, 5, 5]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [10, 9, 8, 7, 6, 5]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [1, 2, 3, 4, 5, 6]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [5, 1, 3, 1, 6, 4, 8]
n = len(data)
assert profit_day(n,data) == true_solving(n, data)

data = [1, 6, 2, 6, 2, 6, 2, 6]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [2, 6, 2, 6, 2, 6]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [3, 6, 2, 4, 1, 2]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [3, 6, 2, 6, 1, 3]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [3, 6, 2, 6, 1, 4]
n = len(data)
print(profit_day(n, data), true_solving(n, data))
assert profit_day(n, data) == true_solving(n, data)

data = [10, 3, 5, 4, 11, 9]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [1, 1, 1, 5, 5, 5, 1, 1, 1, 5, 5, 5, 1, 1, 1]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [2, 2, 2, 5, 5, 5, 1, 1, 1, 5, 5, 5, 2, 2, 2]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [2, 6, 2, 4]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [3, 6, 3, 6, 2, 7]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [4, 10, 2, 9]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [4, 10, 5, 12]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [4, 10, 5, 12, 1]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [1, 6, 4, 8, 3, 6]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)

data = [6, 4, 8, 3, 6, 1]
n = len(data)
assert profit_day(n, data) == true_solving(n, data)
