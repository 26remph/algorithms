import time


def fibonachi(n):

    if n == 0 or n == 1:
        return 1

    return fibonachi(n - 1) + fibonachi(n - 2)


start_time = time.time()

n = 32
# n = int(input())
print(fibonachi(n))
print("--- %s seconds ---" % (time.time() - start_time))
