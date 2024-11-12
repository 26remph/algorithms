import collections
import random
import time


def sqrt_sol(n, k, s):
    # print(s)
    dist = 0
    for i in range(n):
        for j in range(i, n):
            cnt = collections.Counter(s[i : j + 1])
            flags = [not val < k for val in cnt.values()]
            if all(flags):
                dist = max(j - i + 1, dist)

    return dist


def markup(marks: list, letter: dict, limit: int):
    flag = False
    for val in letter.values():
        if val[0] < limit:
            for j in range(1, len(val)):
                # print('j:', j)
                marks[val[j]] = 0
                flag = True

    return flag


def solution(n, k, s):
    marks = []
    cnt = collections.Counter(s)
    for ch in s:
        marks.append(0 if cnt[ch] < k else 1)

    # print('s:', s)
    # print('init', marks)
    # br = 0

    letter = collections.defaultdict(lambda: [0])  # [count, indexs]

    is_cont = True
    while is_cont:
        is_cont = False
        for i in range(n):
            if marks[i] > 0:
                letter[s[i]][0] += 1
                letter[s[i]].append(i)
            else:
                # print('i', i, 'letter', letter)
                if markup(marks, letter, k):
                    is_cont = True
                # print('marks:', marks, 'flag:', is_cont)
                letter.clear()

        if letter:
            # print('_i', i, '_letter', letter)
            if markup(marks, letter, k):
                is_cont = True
            # print('_marks:', marks, '_flag:', is_cont)
            letter.clear()

        # br += 1
        # if br == 10:
        #     break

    # print('marks:', marks)
    ans, cnt = 0, 0
    for i in range(n):
        if marks[i] > 0:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)

    # print('ans', ans)
    return ans


if __name__ == "__main__":
    from string import ascii_lowercase
    # limit_str = ''.join([random.choice(ascii_lowercase) for _ in range(100)])
    # print(limit_str)
    # test_cases = [
    #     ('aaabb', 3, 3),
    #     ('aa', 3, 0),
    #     ('abcab', 2, 0),
    #     ('dabababdeda', 3, 6),
    #     ('ababbc', 2, 5),
    #     ('ababbc', 2, 5),
    #     ('aaabbbbbbbbbcccdeeedd', 3, 21),
    #     ('abababdedabababd', 3, 6),
    #     ('abaccc', 2, 3),
    #     ('aaabccccdeeeebfff', 2, 4),
    #     ('abce', 2, 0),
    #     ('ljjfivqlj', 2, 2),
    #     ('a', 1, 1),
    #     ('abfcaabgac', 2, 2),
    #     ('adaabgac', 2, 2),
    #     ('bsaaa', 3, 3),
    #     ('qqewww', 2, 3),
    # ]
    # n, k = map(int, input().split())
    # s = input()
    # print(solution(n, k, s))

    # for s, k, answer in test_cases:
    #     assert solution(len(s), k, s) == answer
    #
    # print('done')

    tests = [
        (6, 3, "absaaa", 3),
        (5, 3, "aaabb", 3),
        (6, 2, "ababbc", 5),
        (18, 3, "dabababdedabababdd", 9),
        (21, 3, "aaabbbbbbbbbcccdeeedd", 21),
        (16, 3, "abababdedabababd", 6),
        (4, 2, "abce", 0),
        (17, 2, "aaabccccdeeeebfff", 4),
        (6, 2, "abaccc", 3),
        (10, 2, "caaabaaaad", 4),
        (1, 1, "f", 1),
        (2, 1, "fd", 2),
        (10, 10, "ffffffffff", 10),
        (10, 10, "ffffffzfff", 0),
        (10, 1, "qwertyuiop", 10),
        (10, 1, "qqwweerrtt", 10),
        (18, 3, "qweqwertyrtyuiouio", 0),
        (21, 3, "qweqwertyrtyuiouioqwe", 0),
        (21, 3, "qweqweqwertyrtyuiouio", 9),
        (2, 2, "fd", 0),
        (2, 2, "ff", 2),
        (8, 2, "ffgdfhjt", 2),
        (10, 2, "ffffdhhhhh", 5),
        (10, 2, "qwfffffhzx", 5),
        (10, 2, "qwfffffhzx", 5),
        (2, 2, "qq", 2),
        (3, 2, "qqe", 2),
        (6, 2, "qqewww", 3),
        (15, 2, "qqewwwterererer", 8),
        (14, 2, "qqewwwerererer", 14),
        (5, 2, "asdas", 0),
        (2, 2, "aa", 2),
        (6, 3, "ababbc", 0),
        (5, 3, "aaabb", 3),
        (11, 3, "dabababdeda", 6),
        (21, 4, "aaabbbbbbbbbcccdeeedd", 9),
        (16, 3, "abababdedabababd", 6),
        (9, 2, "ljjfivqlj", 2),
        (6, 2, "abaccc", 3),
        (4, 5, "aaaa", 0),
        (8, 4, "ccccaaac", 4),
        (1, 2, "c", 0),
        (6, 3, "aaabbb", 6),
        (7, 2, "ktfkfyq", 0),
        (8, 2, "mpmujprd", 0),
        (18, 2, "afepdjfsfcsryvbjno", 0),
        (
            147,
            3,
            "skudbeyfjqgbmrsuqmemedydnhthdhtvlnxhirlwfhqxptlgscarglvnhxgnsetzxekhybtsiedgqvzthrifwppittevxgfexukbxoxtadxjhipyzkykneneandlqxpwgsbgsvbryrxbquwoenw",
            0,
        ),  # noqa: E501
        (14, 2, "yhdjyuucicniio", 0),
    ]

    # for n, k, s, res in tests:
    #     assert solution(len(s), k, s) == res, f'sol: {solution(len(s), k, s)} res: {res}, s: {s}'  # noqa: E501
    #     assert sqrt_sol(len(s), k, s) == res, f'sol: {sqrt_sol(len(s), k, s)} res: {res}, s: {s}'  # noqa: E501
    #     sqrt = sqrt_sol(n, k, s)
    #     sol = solution(n, k, s)
    #     assert sqrt == sol, f'n:{n} k:{k} s:{s} -> sqrt: {sqrt} != sol: {sol}'

    # cnt = 1
    # base = 1
    # while True:
    #     n = random.randint(1, base)
    #     k = random.randint(1, base)
    #     wrds = [random.choice(ascii_lowercase) for _ in range(n)]
    #     s = ''.join(wrds)
    #     assert sqrt_sol(n, k, s) == solution(n, k, s), f'n:{n} k:{k} s:{s}'
    #
    #     if cnt % 10_000 == 0:
    #         print('cnt:', cnt, 'base:', base, '|', 'n', n, 'k', k, 's', s)
    #         base += 1
    #
    #     cnt += 1
    #
    #     if cnt == 1_000_000:
    #         break

    cnt = 1
    base = 200_000
    while cnt < 10:
        n = base
        k = random.randint(1, base)
        wrds = [random.choice(ascii_lowercase) for _ in range(n)]
        s = "".join(wrds)

        t = time.time()
        res = solution(n, k, s)
        print(time.time() - t, "(s)")

        cnt += 1

    print("done")
