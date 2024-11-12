import collections


def solution(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    for i in range(len(s2)):
        ch1, ch2 = s1[i], s2[i]

        if ch1 != ch2:
            for j in range(len(s1)):
                if s1[j] == ch1:
                    s1[j] = ch2
                elif s1[j] == ch2:
                    s1[j] = ch1

    # print('s1', s1, 's2', s2)
    ans = "YES"
    if s1 != s2:
        ans = "NO"

    return ans


def sol(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    indexes = collections.defaultdict(list)
    for i in range(len(s1)):
        indexes[s1[i]].append(i)

    for i in range(len(s2)):
        ch1, ch2 = s1[i], s2[i]

        if ch1 != ch2:
            for j in indexes[ch1]:
                s1[j] = ch2

            for j in indexes[ch2]:
                s1[j] = ch1

            indexes[ch1], indexes[ch2] = list(indexes[ch2]), list(indexes[ch1])

    ans = "YES"
    if s1 != s2:
        ans = "NO"

    return ans


def sol_fast(s1, s2):
    ind_s1 = collections.defaultdict(list)
    ind_s2 = collections.defaultdict(list)

    for i in range(len(s1)):
        ind_s1[s1[i]].append(i)
        ind_s2[s2[i]].append(i)

    for i in range(len(s1)):
        if ind_s1[s1[i]] != ind_s2[s2[i]]:
            return "NO"

    return "YES"


def sol_dict(s1, s2):
    d1 = {}
    d2 = {}
    for i in range(len(s2)):
        val1 = d1.get(s1[i], None)
        val2 = d2.get(s2[i], None)

        if val1 is None:
            d1[s1[i]] = s2[i]
        else:
            if val1 != s2[i]:
                return "NO"

        if val2 is None:
            d2[s2[i]] = s1[i]
        else:
            if val2 != s1[i]:
                return "NO"

    return "YES"


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s1 = input()
        s2 = input()
        # print(solution(s1, s2))
        # print(sol(s1, s2))
        # print(sol_fast(s1, s2))
        print(sol_dict(s1, s2))

    # tests = [
    #     ('a', 'b', 'YES'),
    #     ('aa', 'bc', 'NO'),
    #     ('aba', 'xbx', 'YES'),
    #     ('abb', 'jjj', 'NO'),
    #     ('abcd', 'pqrs', 'YES'),
    #     ('abc', 'zyc', 'YES'),
    #     ('sssss', 'ppppp', 'YES'),
    #     ('xx', 'ab', 'NO'),
    #     ('abc', 'aaa', 'NO'),
    #     ('abc', 'jjj', 'NO'),
    #     ('abc', 'bac', 'YES'),
    #     ('abc', 'xbc', 'YES'),
    #     ('aba', 'bbb', 'NO'),
    #     ('axa', 'bbb', 'YES'),
    # ]
    #
    # for s1, s2, res in tests:
    #     assert solution(s1, s2) == res, f's1 {s1}, s2 {s2}, res {res}'

    # s1 = 'a' * 50_000
    # s2 = 'b' * 50_000
    # s1 = [random.choice(string.ascii_lowercase) for _ in range(10_000)]
    # s2 = [random.choice(string.ascii_lowercase) for _ in range(10_000)]

    # t = time.time()
    # print(solution(s1, s2))
    # print(time.time() - t, '(s)')

    # for _ in range(10_000):
    #     s1 = [random.choice(string.ascii_lowercase) for _ in range(10)]
    #     s2 = [random.choice(string.ascii_lowercase) for _ in range(10)]

    # s1 = 'px'
    # s2 = 'kk'
    # print('solution:', solution(s1, s2))
    # print('answer:', sol_dict(s1, s2))
    # assert solution(s1, s2) == sol_dict(s1, s2), f'{s1}, {s2}'
