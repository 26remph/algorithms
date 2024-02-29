from timeit import timeit


def fib(n):
    if n in (0, 1):
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_nr(n):
    f1, f2 = 1, 1
    for i in range(n - 1):
        f1, f2 = f2, f1 + f2


def fib_cash(n):
    global count
    count += 1
    if n not in cash:
        cash[n] = fib_cash(n - 1) + fib_cash(n - 2)

    return cash[n]


if __name__ == '__main__':
    print(f'{timeit("fib(35)", number=10, globals=globals()) / 10} c.')
    print(f'{timeit("fib_nr(35)", number=10, globals=globals()) / 10} c.')
    count = 0
    cash = {0: 1, 1: 1}
    print(f'res={fib_cash(35)}, count={count}')
