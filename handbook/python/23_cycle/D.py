n = int(input())
m = int(input())

step = 1 if n < m else -1
n, m = (n, m + 1) if n < m else (n, m - 1)

ans = []
for i in range(n, m, step):
    ans.append(str(i))

print(" ".join(ans))
