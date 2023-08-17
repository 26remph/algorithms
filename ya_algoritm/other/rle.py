from collections import deque
from string import ascii_lowercase


def solution(s):

    steak = []
    for i in range(len(s)):

        if s[i] == ']':
            cur = deque()
            while steak and (ch := steak.pop()) != '[':
                cur.appendleft(ch)
            num = steak.pop()
            steak.append(''.join(cur) * int(num))
        else:
            steak.append(s[i])

    return ''.join(steak)



def solution_recursion(s):


    def dfs(cur):

        for i in range(len(s)):

            cur += s[i]

            if s[i] == '[':
                dfs(cur)
            else:
                ...

        # return res

    return dfs('')


if __name__ == '__main__':
    # s = input()
    tests = [
        ('2[4[2[b]]]', 'bbbbbbbbbbbbbbbb'),
        ('4[ba]', 'babababa'),
        ('2[3[a]3[b]a]', 'aaabbbaaaabbba'),
        ('2[3[a]3[b]]', 'aaabbbaaabbb'),
        ('2[2[2[b2[a]]]]', 'baabaabaabaabaabaabaabaa'),
        ('2[ab3[as]]1[a]', 'abasasasabasasasa'),
        ('1[1[1[abc]]]', 'abc'),
        ('2[abc]1[de]3[f]', 'abcabcdefff'),
        ('2[1[2[a]b3[c]]]', 'aabcccaabccc'),
        ('ab2[ac2[ab]]', 'abacababacabab')
    ]
    # print(solution(s))
    for s, ans in tests:
        print(solution(s))
        assert solution(s) == ans, f'{s=}, {solution(s)} != {ans}'
