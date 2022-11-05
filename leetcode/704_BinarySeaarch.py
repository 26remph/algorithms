from bisect import bisect_left
from typing import List
import random


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        return i if i != len(nums) and nums[i] == target else -1



    def clasic_binary(self, nums: List[int], target: int) -> int:

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + ((hi - lo + 1) // 2)
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid

        return lo if nums[lo] == target else -1


def gen_sample(arr_len, num_len):
    result = []
    for i in range(arr_len):
        result.append(random.randint(-num_len, num_len))
    result.sort()
    index = random.randint(0, arr_len - 1)
    return result, index, result[index]


MAX_NUM = 10_000
MAX_ARR_LEN = 10

sol = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9
assert sol.search(nums, target) == sol.clasic_binary(nums, target)
target = 2
assert sol.search(nums, target) == sol.clasic_binary(nums, target)


nums = [-1, 0, 3]
target = -1
assert sol.search(nums, target) == sol.clasic_binary(nums, target)

nums = [-9953, -7712, -5408, -5404, -4300, -2584, 3075, 9776, 9973, 9973]
target = 9973
assert sol.search(nums, target) == sol.clasic_binary(nums, target)

nums = [0, 8, 8, 8, 9]
target = 8
assert sol.search(nums, target) == sol.clasic_binary(nums, target)

for test in range(10_000):
    nums, ind, target = gen_sample(MAX_ARR_LEN, MAX_NUM)
    assert sol.search(nums, target) == ind, (target, ind, nums)
    assert sol.clasic_binary(nums, target) == ind, (target, ind, nums)

print(f"\033[92m complete")
