from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        pairs = 0
        for key, value in cnt.items():
            pairs += value // 2

        pairs *= 2
        print(pairs)
        if sum(cnt.values()) > pairs:
            pairs += 1

        return pairs


sol = Solution()
s = "abccccdd"
assert sol.longestPalindrome(s) == 7
s = "a"
assert sol.longestPalindrome(s) == 1