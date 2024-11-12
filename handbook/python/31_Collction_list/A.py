N = int(input())
ans = "YES"
for _ in range(N):
    if not input().capitalize().startswith(("А", "Б", "В")):
        ans = "NO"

print(ans)
