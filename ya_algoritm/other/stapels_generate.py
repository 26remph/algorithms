def solution():

    ans = []
    def gen(res, op, cl):

        if len(res) == n:
            ans.append(res)
            return res

        gen(res+'(', op+1, cl)

        if cl < op:
            res += ')'
            cl += 1
            gen(res, op, cl)

    gen('', 0, 0)

    # for i in range(len(ans)):
    #     s = ans[i]
    #     ext = ''
    #     for j in range(len(s) - 1, -1, -1):
    #         ext += '(' if s[j] == ')' else ')'
    #     s += ext
    #     ans[i] = s

    return ans


if __name__ == '__main__':
    n = int(input())
    tests = [
        (('()'), 1),
        (('(())', '()()'), 2),
        (('(()())', '((()))', '()()()', '(())()', '()(())'), 3),
        (('(((())))', '((()()))', '()()()()', '()(())()', '(()()())'), 4),
    ]
    print(solution())
    # print(' '.join(solution()))
