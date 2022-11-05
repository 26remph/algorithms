class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        judje_fw = {}
        judje_back = {}
        for i in range(len(s)):
            forward = judje_fw.get(s[i])
            if not forward:
                judje_fw[s[i]] = t[i]
            else:
                if forward != t[i]:
                    return False

            reverse = judje_back.get(t[i])
            if not reverse:
                judje_back[t[i]] = s[i]
            else:
                if reverse != s[i]:
                    return False

        return True

    def isIsomorphicShort(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == list(map(t.find, t))


sol = Solution()
s = "egg"
t = "add"
assert sol.isIsomorphic(s, t) == sol.isIsomorphicShort(s, t)

s = "foo"
t = "bar"
assert sol.isIsomorphic(s, t) == sol.isIsomorphicShort(s, t)

s = "paper"
t = "title"
assert sol.isIsomorphic(s, t) == sol.isIsomorphicShort(s, t)

s = "badc"
t = "baba"
assert sol.isIsomorphic(s, t) == sol.isIsomorphicShort(s, t)
