r = int(input())
i = int(input())
c = int(input())

ans = i
if i == 0:
    ans = 3 if r != 0 else c
if i == 1:
    ans = c
if i == 4:
    ans = 3 if r != 0 else 4
if i == 6:
    ans = 0
if i == 7:
    ans = 1

print(ans)
