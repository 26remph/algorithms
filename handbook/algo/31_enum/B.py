from math import factorial


n, k = map(int, input().split())
if n < k:
    print(0)
else:
    print(int(factorial(n) / (factorial(k) * factorial(n - k))))
    # print(int(factorial(n) / (factorial(n - k))))
