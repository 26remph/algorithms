from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zeros = 0
        ans = 0

        j = 0
        for i in range(len(nums)):

            while j < len(nums) and zeros < 2:
                if nums[j] == 0:
                    zeros += 1
                j += 1

            ans = max(ans, j - i - zeros)
            if nums[i] == 0:
                zeros -= 1

            if j >= len(nums):
                break

        if ans == len(nums):
            ans -= 1

        return ans

    def longestSubarray_without_slice(self, nums: List[int]) -> int:

        z_cnt = 0
        total = 0
        left_summ = 0
        max_summ = 0
        for ch in nums:

            if ch == 1:
                if z_cnt < 1:
                    left_summ += 1
                total += 1
            else:
                z_cnt += 1

                if z_cnt > 1:
                    left_summ = total - left_summ
                    max_summ = max(total, max_summ)
                    z_cnt = 1
                    total = left_summ

        max_summ = max(total, max_summ)
        if max_summ == len(nums):
            max_summ -= 1

        return max_summ


if __name__ == '__main__':
    tests = (
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
        ([0, 0], 0),
        ([1], 0),
        ([1, 1, 0, 0, 1, 1, 1, 0, 1], 4),
    )

    sol = Solution()
    for arr, res in tests:
        ans = sol.longestSubarray(arr)
        assert ans == res, f'{ans=}, {res=}, {arr=}'
