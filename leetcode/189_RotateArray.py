from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        deq = deque(nums)
        deq.rotate(k)
        nums.clear()
        nums.extend(deq)
        return nums

    def rotate_v2(self, nums: List[int], k: int) -> None:
        for step in range(k):
            val = nums.pop()
            nums.insert(0, val)

        return nums

    def rotate_v3(self, nums: List[int], k: int) -> None:
        print(nums)
        j = 0
        for i in range(len(nums)):
            narrow = (i + k) % len(nums)
            print(narrow, i)
            # nums[narrow] = pointer[i]
            if i > 3:
                break
                save = nums[narrow]
                nums[narrow] = nums[j]
                nums[j] = save
                j += 1
                if j == 3:
                    break
            else:
                save = nums[narrow]
                nums[narrow] = nums[i]
                nums[i] = save

        print(nums)
        return nums


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
assert sol.rotate(nums, k) == [5, 6, 7, 1, 2, 3, 4]
# assert sol.rotate(nums, k) == sol.rotate_v2(nums, k)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 4
assert sol.rotate_v3(nums, k) == [8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7]


nums = [-1, -100, 3, 99]
k = 2
# assert sol.rotate(nums, k) == [3, 99, -1, -100]
# assert sol.rotate_v2(nums, k) == [3, 99, -1, -100]
assert sol.rotate_v3(nums, k) == [3, 99, -1, -100]
