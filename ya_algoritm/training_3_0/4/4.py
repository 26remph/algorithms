n = int(input())
k = int(input())
r = int(input())
m = int(input())

num = r * 2 - m % 2
var_1 = num + k if (num + k) <= n else None
var_2 = num - k if num - k > 0 else None

ans = -1
if all([var_1, var_2]):
    r1 = var_1 // 2 + var_1 % 2
    r2 = var_2 // 2 + var_2 % 2

    ans = var_2 if abs(r2 - r) < abs(r1 - r) else var_1

elif var_1:
    ans = var_1

elif var_2:
    ans = var_2


# print('ans:', ans)
if ans > 0:
    print(ans // 2 + ans % 2, 2 if ans % 2 == 0 else 1)
else:
    print(ans)
