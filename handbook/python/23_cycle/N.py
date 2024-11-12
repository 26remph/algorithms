import random


n = int(input())

test_cnt = 100

ans = "YES" if n > 1 else "NO"
if n > 1:
    for _ in range(test_cnt):
        a = random.randint(1, n - 1)
        if pow(a, n - 1, n) != 1:
            ans = "NO"
            break

print(ans)
