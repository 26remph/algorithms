import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2[: len(s1)])

        for i in range(len(s1), len(s2)):
            # print(f'{i=}', d1, d2)
            if len(d1) == len(d2) and d1 == d2:
                return True

            d2[s2[i]] += 1
            if d2[s2[i - len(s1)]] - 1:
                d2[s2[i - len(s1)]] -= 1
            else:
                del d2[s2[i - len(s1)]]

        return bool(len(d1) == len(d2) and d1 == d2)

    def slow_checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        deq = collections.deque()
        j = 0
        for _ in range(len(s2)):
            while j < len(s2) and len(deq) < len(s1):
                deq.append(s2[j])
                j += 1

            if s1 == "".join(sorted(deq)):
                return True

            deq.popleft()

        return False


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    sol = Solution()
    print(sol.checkInclusion(s1, s2))
