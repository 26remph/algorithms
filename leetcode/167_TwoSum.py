from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]


sol = Solution()

numbers = [2, 7, 11, 15]
target = 9
assert sol.twoSum(numbers, target) == [1, 2]


numbers = [2, 3, 4]
target = 6
assert sol.twoSum(numbers, target) == [1, 3]

numbers = [-1, 0]
target = -1
assert sol.twoSum(numbers, target) == [1, 2]