import collections

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(p):
            return p and int(p) <= 255 and str(int(p)) == p

        path = collections.deque()
        for i in range(3):
            if is_valid(s[: i + 1]):
                path.append(s[: i + 1])

        ans = []
        while path:
            prefix = path.popleft()
            len_ip = len(prefix.split("."))

            if len_ip == 4:
                ans.append(prefix)

            st = len("".join(prefix.split(".")))
            if len_ip == 3 and is_valid(s[st:]):
                prefix += "." + s[st:]
                path.append(prefix)

            if len_ip < 3:
                for i in range(1, 4):
                    if is_valid(s[st : st + i]):
                        path.append(prefix + "." + s[st : st + i])

        return ans

    def dfs_restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(p):
            if not p or int(p) > 255:
                return False

            return str(int(p)) == p

        ip = []
        ans = []

        def dfs(sub):
            prefix = ""
            for i in range(len(sub)):
                if len(ip) == 3:
                    prefix = sub[i:]
                else:
                    prefix += sub[i]
                if is_valid(prefix):
                    ip.append(prefix)
                    dfs(sub[i + 1 :])
                    if len(ip) == 4 and len("".join(ip)) == len(s):
                        ans.append(".".join(ip))
                    ip.pop()

        dfs(s)
        return ans


if __name__ == "__main__":
    s = "25525511135"
    # s = '0000'
    # s = '101023'
    # s = '10101010'
    sol = Solution()
    print(sol.restoreIpAddresses(s))
    # print(sol.dfs_restoreIpAddresses(s))
