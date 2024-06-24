n, m = map(int, input().strip().split(' '))
inf = float('inf')
arr = [[inf for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().strip().split(' ')))
    for j in range(1, m + 1):
        arr[i][j] = row[j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        _min = min(arr[i - 1][j], arr[i][j - 1])
        if i == j == 1:
            continue
        arr[i][j] = arr[i][j] + _min

print(arr[-1][-1])
# for i in range(n+1):
#     print(f'{i}: {arr[i]}')
