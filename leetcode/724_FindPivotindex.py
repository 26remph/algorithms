from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        l_acc = [0] * len(nums)
        r_acc = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            l_acc[i] = l_acc[i + 1] + nums[i + 1]

        for i in range(1, len(nums)):
            r_acc[i] = r_acc[i - 1] + nums[i - 1]

        for i in range(len(l_acc)):
            if l_acc[i] == r_acc[i]:
                return i

        return -1

if __name__ == '__main__':
    sol = Solution()
    arr = [1, 7, 3, 6, 5, 6]
    assert sol.pivotIndex(arr) == 3
    arr = [1, 2, 3]
    assert sol.pivotIndex(arr) == -1
    arr = [2, 1, -1]
    assert sol.pivotIndex(arr) == 0
    arr = [0, 0, 0, 0]
    assert sol.pivotIndex(arr) == 0
    arr = [0, 0]
    assert sol.pivotIndex(arr) == 0
    arr = [-1, 1]
    assert sol.pivotIndex(arr) == -1
    arr = [6, 6, 6, 6, 6, 6, 6]
    assert sol.pivotIndex(arr) == 3
    arr = [-1, 8]
    assert sol.pivotIndex(arr) == -1




