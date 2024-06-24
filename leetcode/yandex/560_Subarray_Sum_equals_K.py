import collections

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        prefix_summ = collections.defaultdict(int)
        prefix_summ[0] = 1
        for n in nums:
            total += n
            prefix = total - k
            ans += prefix_summ.get(prefix, 0)
            prefix_summ[total] += 1

        return ans

    def squad_subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 0
        for i in range(len(prefix)):
            for j in range(i + 1, len(prefix)):
                if prefix[j] - prefix[i] == k:
                    ans += 1

        return ans


if __name__ == '__main__':
    test = (
        ([1, -1, 0], 0, 3),
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0),
    )

    sol = Solution()
    for nums, k, out in test:
        res = sol.subarraySum(nums, k)
        print(res)
        assert out == res, f'{out=}, {res=}, {nums=}'