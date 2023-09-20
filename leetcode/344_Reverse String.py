from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s


sol = Solution()
s = ["h", "e", "l", "l", "o"]
assert sol.reverseString(s) == ["o","l","l","e","h"]

s = ["H", "a", "n", "n", "a", "h"]
assert sol.reverseString(s) == ["h","a","n","n","a","H"]