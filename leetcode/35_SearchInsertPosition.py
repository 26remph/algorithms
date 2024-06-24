from bisect import bisect_left
from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        return i

    def searchfastInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l


sol = Solution()
nums = [1, 3, 5, 6]
target = 5
assert sol.searchInsert(nums, target) == sol.searchfastInsert(nums, target)
target = 2
assert sol.searchInsert(nums, target) == sol.searchfastInsert(nums, target)
target = 7
assert sol.searchInsert(nums, target) == sol.searchfastInsert(nums, target)
