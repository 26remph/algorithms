from itertools import product


n = int(input())
m = int(input())
line = 0
frmt = len(str(n * m))
for x, y in product(range(n), range(1, m + 1)):

    if x > line:
        print('')
        line += 1

    res = x * m + y
    print(f'{res:{frmt}d}', end=' ')

# print('')
# print(list(product(range(1, n + 1), range(1, m + 1))))
