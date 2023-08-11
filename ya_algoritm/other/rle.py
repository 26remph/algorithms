from string import ascii_lowercase

def solution(s):


    def dfs(res, open, close, ind):

        if s[ind] == close:
            return res

        num = 0
        for i in range(ind, len(s)):
            if s[i] == open:
                res = dfs(res, open, close, i + 1)
                res += res * num if num else 1

            if s[i] not in ascii_lowercase:
                num = int(s[i])
            else:
                res += s[i] * num if num else 1

        return res

    return dfs('', '[', ']', 0)


if __name__ == '__main__':
    s = input()
    tests = [
        ('2[4[2B]]', 'BBBBBBBBBBBBBBBBBBBB'),
        ('4[BA]]', 'BABABABA'),
        ('2[3A3B]', 'AAABBBAAABBB'),
        ('2[2[2[B2A]]', 'BAABAABAABAABAABAABAABAA'),
    ]
    print(solution(s))
    for s, ans in tests:
        assert solution(s) == ans, f's={s}, {solution(s)} != {ans}'
