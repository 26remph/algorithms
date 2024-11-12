n = int(input())

ans = "YES" if n > 1 else "NO"
for i in range(2, int(pow(n, 0.5)) + 1):
    if n % i == 0:
        ans = "NO"

print(ans)
