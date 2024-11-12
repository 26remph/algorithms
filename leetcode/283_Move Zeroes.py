from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                continue

            if j == len(nums):
                break

            if j < i:
                j = i + 1

            while j < len(nums):
                if nums[j] == 0:
                    j += 1
                    continue

                nums[i] = nums[j]
                nums[j] = 0
                j += 1
                break

            i += 1

        return nums

    def moveZeroes_swap(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums


sol = Solution()
nums = [0, 1, 0, 3, 12]
assert sol.moveZeroes(nums) == [1, 3, 12, 0, 0]

nums = [0, 1, 0, 3, 12]
assert sol.moveZeroes_swap(nums) == [1, 3, 12, 0, 0]


nums = [0]
assert sol.moveZeroes(nums) == [0]
