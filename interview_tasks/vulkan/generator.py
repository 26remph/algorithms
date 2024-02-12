def sample_gen(N):
    for i in range(N):
        yield i


a, b, *c = sample_gen(4)
print(f'{a=}, {b=}, {c=}')


def increment(x):
    x += 1
    return x


x = 10
print(increment(x))
print(x)

import sys
arr_1 = []
arr2 = arr_1
print(sys.getrefcount(arr_1))