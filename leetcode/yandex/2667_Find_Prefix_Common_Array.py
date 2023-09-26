from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []

        setA = set()
        setB = set()

        total = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                total += 1
            elif A[i] in setB and B[i] in setA:
                total += 2
            elif A[i] in setB or B[i] in setA:
                total += 1

            ans.append(total)
            setA.add(A[i])
            setB.add(B[i])

        return ans


if __name__ == '__main__':
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    # A = [2, 3, 1]
    # B = [3, 1, 2]
    sol = Solution()
    print(sol.findThePrefixCommonArray(A, B))