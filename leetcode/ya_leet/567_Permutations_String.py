import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(list(s1)))
        deq = collections.deque()
        j = 0
        for i in range(len(s2)):
            while j < len(s2) and len(deq) < len(s1):
                deq.append(s2[j])
                j += 1

            if s1 == ''.join(sorted(deq)):
                return True

            deq.popleft()

        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    sol = Solution()
    print(sol.checkInclusion(s1, s2))