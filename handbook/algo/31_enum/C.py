from math import factorial

n, k = map(int, input().split())
if n < k:
    print(0)
else:
    print(int(factorial(n + k - 1) / (factorial(k) * factorial(n - 1))))
