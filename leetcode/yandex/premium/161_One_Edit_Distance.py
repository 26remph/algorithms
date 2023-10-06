# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
# A string s is said to be one distance apart from a string t if you can:
# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if len(s) < len(t):
            s, t = t, s

        if len(s) - len(t) > 1 or s == t:
            return False

        for i in range(len(t)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] if len(s) == len(t) else s[i+1:] == t[i:]

        return True


if __name__ == '__main__':
    test = [
        ('abef', 'acbef', True),
        ('a', '', True),
        ('acbref', 'acbef', True),
        ('acgef', 'acbef', True),
        ('ab', 'acbef', False),
        ('abcvfdrhfjhs', 'acbef', False),
        ('acbef', 'acbef', False),
    ]
    sol = Solution()
    for s, t, ans in test:
        res = sol.isOneEditDistance(s, t)
        assert res == ans, f'{s=}, {t=}, {ans=}, {res}'
