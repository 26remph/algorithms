n, m = map(int, input().split())
a = []
for _ in range(n * 2):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    for j in range(m):
        print(a[i][j] + a[i + n][j], end=" ")
    print("")
