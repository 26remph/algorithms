import collections

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pkey = [0] * 26
        skey = [0] * 26

        for ch in p:
            pkey[ord(ch) - ord('a')] += 1

        ans = []
        for i in range(len(s)):
            if i < len(p):
                skey[ord(s[i]) - ord('a')] += 1
                continue

            if pkey == skey:
                ans.append(i - len(p))

            skey[ord(s[i]) - ord('a')] += 1
            skey[ord(s[i - len(p)]) - ord('a')] -= 1

        if pkey == skey:
            ans.append(len(s) - len(p))

        return ans

    def dict_findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = collections.Counter(p)
        d2 = collections.Counter(s[:len(p)])

        ans = []
        for i in range(len(p), len(s)):

            if len(d2) == len(d1) and d1 == d2:
                ans.append(i - len(p))

            d2[s[i]] += 1

            if d2[s[i - len(p)]] - 1:
                d2[s[i - len(p)]] -= 1
            else:
                del d2[s[i - len(p)]]

        if len(d1) == len(d2) and d1 == d2:
            ans.append(len(s) - len(p))

        return ans


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    # out = [0, 6]

    # s = "abab"
    # p = "ab"
    # out = [0, 1, 2]

    sol = Solution()
    print(sol.findAnagrams(s, p))
