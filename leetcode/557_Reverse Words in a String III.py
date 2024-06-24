class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for ind, word in enumerate(arr):
            words = list(word)
            i, j = 0, len(words) - 1
            while i < j:
                words[i], words[j] = words[j], words[i]
                i += 1
                j -= 1

            arr[ind] = ''.join(words)

        return ' '.join(arr)


sol = Solution()
s = "Let's take LeetCode contest"

assert sol.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

s = "God Ding"
assert sol.reverseWords(s) == "doG gniD"