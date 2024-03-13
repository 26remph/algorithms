import random


def main():
    if p + v >= q + m and p - v <= q - m:
        return abs(v) * 2 + 1

    if q + m >= p + v and q - m <= p - v:
        return abs(m) * 2 + 1

    if p - v > q + m:
        return abs(v) * 2 + abs(m) * 2 + 2

    if p - v == q - m:
        return abs(v) * 2 + abs(m) * 2 + 1

    if q - m > p + v:
        return abs(v) * 2 + abs(m) * 2 + 2

    if q - m == p + v:
        return abs(v) * 2 + abs(m) * 2 + 1

    if q > p:
        d = abs((p + v) - (q - m)) + 1
        return abs(v) * 2 + abs(m) * 2 + 2 - d

    if p > q:
        d = abs((p - v) - (q + m)) + 1
        return abs(v) * 2 + abs(m) * 2 + 2 - d


# p, v = map(int, input().split())
# q, m = map(int, input().split())
# print(main())

if __name__ == '__main__':

    tests = [
        (2, 2, 1, 1, 5),
        (2, 1, 2, 0, 3),
        (2, 1, 1, 0, 3),
        (2, 2, 0, 0, 5),
        (2, 2, 3, 1, 5),
        (2, 2, 4, 0, 5),
        (2, 2, 1, 3, 7),
        (2, 0, 1, 3, 7),
        (-2, 2, -1, 1, 5),
        (0, 0, 0, 0, 1),
        (0, 1, 3, 2, 7),
        (-2, 2, 0, 1, 6),
        (3, 1, -2, 0, 4),
        (0, 1, 3, 2, 7),
        (-2, 2, 0, 1, 6),
        (-1, 2, -2, 2, 6),
        (-1, 2, -2, 2, 6),
        (-1, 2, -2, 2, 6),
        (1, 1, -1, 1, 5),
    ]
    for test in tests:
        p, v, q, m, ans = test
        assert main() == ans, f'{p=}, {v=}, {q=}, {m=}, {ans=}, {main()=}'

    for _ in range(100_000):
        p, v = random.randint(-10, 10), random.randint(0, 10)
        q, m = random.randint(-10, 10), random.randint(0, 10)
        print(len(range(p - v, p + v + 1)), list(range(p - v, p + v + 1)))
        print(len(range(q - m, q + m + 1)), list(range(q - m, q + m + 1)))
        ans_s = set(range(p - v, p + v + 1)) | set(range(q - m, q + m + 1))
        print(ans_s, len(ans_s))

        res = len(set(range(p - v, p + v + 1)) | set(range(q - m, q + m + 1)))
        assert main() == res, f'{main()=}, {res=}, {p=}, {v=}, {q=}, {m=}'
