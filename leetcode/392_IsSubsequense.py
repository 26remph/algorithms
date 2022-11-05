from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        t_pos = defaultdict(list)

        for pos in range(len(t)):
            t_pos[t[pos]].append(pos)

        last_pos = 0
        for pos in range(len(s)):
            if not t_pos.get(s[pos]):
                return False

            flag = False
            for i in t_pos.get(s[pos]):
                if i >= last_pos:
                    last_pos = i + 1
                    flag = True
                    break

            if not flag:
                return False

        return True


sol = Solution()
s = "abc"
t = "ahbgdca"
assert sol.isSubsequence(s, t) == True

s = "axc"
t = "ahbgdc"
assert sol.isSubsequence(s, t) == False

s = "acb"
t = "ahbgdc"
assert sol.isSubsequence(s, t) == False
