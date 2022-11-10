class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        substr = set()
        i, j = 0, 0
        cnt = 0
        while i < len(s):
            while j < len(s):
                if i == j:
                    substr.add(s[i])
                    cnt = max(cnt, len(substr))
                    j += 1
                else:
                    len_before = len(substr)
                    substr.add(s[j])
                    cnt = max(cnt, len(substr))
                    if len_before == len(substr):
                        substr = set()
                        # print(i, j)
                        # print('fp:', s.find(s[j], i, j))
                        pos = s.find(s[j], i, j) + 1
                        i = j = pos
                        # print(i, j, pos)
                    else:
                        j += 1

            break

        return cnt


sol = Solution()
# s = "abcabcbb"
# assert sol.lengthOfLongestSubstring(s) == 3
# s = "bbbb"
# assert sol.lengthOfLongestSubstring(s) == 1
# s = "pwwkew"
# assert sol.lengthOfLongestSubstring(s) == 3
# s = "aab"
# assert sol.lengthOfLongestSubstring(s) == 2
# s = "a"
# assert sol.lengthOfLongestSubstring(s) == 1
# s = "dvdf"
# assert sol.lengthOfLongestSubstring(s) == 3
s = "dvklmdfju"
assert sol.lengthOfLongestSubstring(s) == 8
