from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        lst1 = list(set(nums1) - set(nums2))
        lst2 = list(set(nums2) - set(nums1))

        return [lst1, lst2]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    ans = [[1,3], [4,6]]
    sol = Solution()
    print(sol.findDifference(nums1, nums2))


