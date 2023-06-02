def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def main():
    x, y = map(int, input().split())

    keys = []
    for i in range(x, y + 1):
        if i % x == 0 and y % i == 0:
            keys.append(i)

    print(keys)
    if not keys:
        return 0
    elif len(keys) == 1:
        return 1

    cnt = 0
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            print('-->', keys[i], keys[j])
            if gcd(keys[i], keys[j]) == x and keys[i] * keys[j] / x == y:
                print(keys[i], keys[j])
                cnt += 1

    return cnt * 2


if __name__ == '__main__':
    print(main())