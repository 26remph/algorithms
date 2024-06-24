import time


N = 200_000
W = 5

start = time.time()
x = 0
for _ in range(N):
    for _ in range(W):
        x = x + 2

print(time.time() - start, 'sec')
