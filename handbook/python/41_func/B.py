def gcd_recurse(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    if n2 == 0:
        return n1

    return gcd(n2, n1 % n2)


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1


if __name__ == "__main__":
    test = [
        (1071, 462, 21),
        (0, 0, 0),
        (1, 0, 1),
        (462, 1071, 21),
        (3, 2, 1),
        (6, 3, 3),
        (12, 45, 3),
        (144, 96, 48),
    ]
    for param in test:
        n1, n2, ans = param
        assert gcd(n1, n2) == ans, f"{n1=},{n2=},{ans=}, {gcd(n1, n2)}"

    print("pass")
