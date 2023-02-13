n = int(input())
m = int(input())

ans = []
for i in range(n, m + 1):
    ans.append(i)

print(' '.join(map(str, ans)))

