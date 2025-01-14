import time


t = time.time()
x = 10
for _ in range(1000):
    for _ in range(1000):
        if x == 10:
            x += 1

        if x == 5:
            x += 1

        if x == 4:
            x += 1


print(x)
print(time.time() - t, "(s)")
