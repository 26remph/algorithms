N = int(input())
M = int(input())
K1, K2 = int(input()), int(input())

x = (N * M - K2 * N) / (K1 - K2)
y = N - x
print(int(x), int(y))
