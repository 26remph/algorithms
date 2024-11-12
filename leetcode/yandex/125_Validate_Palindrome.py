import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chrs = string.ascii_letters + string.digits
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in chrs:
                i += 1
                continue
            if s[j] not in chrs:
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama"
    # s = "0P"
    # s = "race a car"
    s = ""
    sol = Solution()
    print(sol.isPalindrome(s))
