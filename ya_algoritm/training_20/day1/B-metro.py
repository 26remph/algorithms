N, i, j = list(map(int, input().split()))

if i < j:
    ans = min(j-i-1, N - j + i - 1)
else:
    ans = min(i-j-1, N - i + j - 1)

print(ans)

