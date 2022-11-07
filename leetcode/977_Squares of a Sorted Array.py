from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [x ** 2 for x in nums]
        arr.sort()
        return arr


sol = Solution()
nums = [-4, -1, 0, 3, 10]
assert sol.sortedSquares(nums) == [0, 1, 9, 16, 100]
nums = [-7, -3, 2, 3, 11]
assert sol.sortedSquares(nums) == [4, 9, 9, 49, 121]

