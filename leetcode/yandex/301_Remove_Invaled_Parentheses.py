import collections
import itertools
from typing import List


class Solution:
    def check(self, path, mode=1):

        close = 0
        stack = 0
        for ch in path:
            if ch == '(':
                stack += 1
            elif ch == ')':
                if stack:
                    stack -= 1
                else:
                    if mode == 2:
                        return float('inf')
                    close += 1

        return stack + close


    def removeInvalidParentheses(self, s: str) -> List[str]:

        col = self.check(s)
        if not col:
            return [s]

        seq = [(ind, ch) for ind, ch in enumerate(s) if ch in '()']

        if not (len(seq) - col):
            return [''.join([ch for ch in s if ch not in '()'])]

        ans = set()
        for c in itertools.combinations(seq, col):

            exclude = {i for i, x in c}
            lst = [ch for i, ch in enumerate(s) if i not in exclude]

            if not self.check(lst, mode=2):
                ans.add(''.join(lst))

        return list(ans) if len(ans) else [""]


if __name__ == '__main__':
    tests = (
        ("()())()", ["(())()", "()()()"]),
        ("(a)())()", ["(a())()", "(a)()()"]),
        (")(", ['']),
        ('(', ['']),
        ('x(', ['x']),
        (')(f', ['f']),
        (')d))', ['d']),
        ("))(", ['']),
        (")()(", ["()"])
    )

    sol = Solution()
    for s, ans in tests:
        res = sol.removeInvalidParentheses(s)
        assert set(ans) == set(res), f'{ans=}, {res=}, {s=}'
