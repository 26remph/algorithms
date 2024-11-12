def gcd_of_two(x, y):
    while y:
        x, y = y, x % y

    return x


def gcd(*args):
    if len(args) == 1:
        return args[0]

    lst = sorted(args)

    x = lst[0]
    for i in range(1, len(lst)):
        y = lst[i]
        while y:
            x, y = y, x % y

    return x


if __name__ == "__main__":
    print(gcd(36, 48, 156, 100500))
    print(gcd(3))
