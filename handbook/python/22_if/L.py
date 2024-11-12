a, b, c = int(input()), int(input()), int(input())

ans = "NO"
if a < b + c and b < a + c and c < a + b:
    ans = "YES"

print(ans)
