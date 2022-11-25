x, y, z = list(map(int, input().split()))

ans = 1
if 12 >= x != y <= 12:
    ans = 0
elif x > 12 and y > 12:
    ans = 0

print(ans)
