import time


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def test10ok(x, y):
    # x, y = map(int, input().split())

    if x == y:
        return 1

    cnt = 0
    lim = int(x + (y - x) / 2)
    for i in range(x, lim):
        if i % x == 0 and y % i == 0:
            j = y * x / i
            if gcd(i, j) == x and i * j / x == y:
                print(i, j)
                cnt += 1

    return cnt + 1 if cnt else cnt


def main(x, y):
    # x, y = map(int, input().split())

    if x == y:
        return 1
    if y % x != 0:
        return 0

    cnt = 2
    for i in range(2, (y // x // 2) + 1):

        a = x * i
        b = y * x / a

        if a >= b:
            break
        if b != int(b):
            continue
        if gcd(a, b) == x:
            cnt += 2

    return cnt


if __name__ == '__main__':

    for _ in range(1_000):
        # x = random.randint(1, 100)
        # y = random.randint(x, 100)
        x, y = map(int, input().split())
        t = time.time()
        # print(test10ok(x, y))
        # print('--->', time.time() - t)
        t = time.time()
        print(main(x, y), time.time() - t, '(sec)')
        # assert main(x, y) == test10ok(x, y), f'x={x}, y={y}'
