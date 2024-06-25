# import time

def fibonachi(n):

    x, y, z = 0, 1, 1

    if n == 0 or n == 1:
        return 1

    for _ in range(n):
        z = (x + y) % 10 ** k
        x, y = y, z

    return z


n, k = map(int, input().strip().split(' '))
# start_time = time.time()
print(fibonachi(n))
# print("--- %s seconds ---" % (time.time() - start_time))
