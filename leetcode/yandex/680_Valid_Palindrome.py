class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return (
                    s[i:j] == s[i:j][::-1] or s[i + 1 : j + 1] == s[i + 1 : j + 1][::-1]
                )
            i += 1
            j -= 1

        return True

    def recursion_validPalindrome(self, s: str, is_deleted=False) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if is_deleted:
                    return False
                return self.validPalindrome(s[i:j], True) or self.validPalindrome(
                    s[i + 1 : j + 1], True
                )

            i += 1
            j -= 1

        return True

    def complex_validPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 2:
            return True

        if len(s) == 3:
            # if s[0] != s[2] and s[0] != s[1]:
            #     return False
            # else:
            #     return True
            return not (s[0] != s[2] and s[0] != s[1])

        cnt = 0
        j = len(s) - 1
        i = 0
        save_i = None
        save_j = None
        flag = True
        while i < j:
            if s[i] != s[j]:
                if not cnt:
                    if s[i + 1] == s[j] and s[j - 1] == s[i]:
                        save_i = i
                        save_j = j - 1
                        i += 1
                    elif s[i + 1] == s[j]:
                        i += 1
                    elif s[j - 1] == s[i]:
                        j -= 1
                    else:
                        return False

                    cnt += 1
                else:
                    if save_i is not None and flag:
                        flag = False
                        i = save_i
                        j = save_j
                    else:
                        return False
            else:
                i += 1
                j -= 1

        return True


if __name__ == "__main__":
    tests = (
        (
            "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip",
            False,
        ),
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("eedede", True),
        ("tcaac", True),
        ("atbbga", False),
        (
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
            True,
        ),
        ("ebcbbececabbacecbbcbe", True),
    )
    sol = Solution()
    for s, ans in tests:
        res = sol.validPalindrome(s)
        # res = sol.complex_validPalindrome(s)
        assert res == ans, f"{res=}, {ans=}, {s=}"
