N, i, j = list(map(int, input().split()))

ans = min(j - i - 1, N - j + i - 1) if i < j else min(i - j - 1, N - i + j - 1)

print(ans)
