import collections

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans

    def many_memory_intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        for k in d2:
            d1[k] = min(d1[k], d2[k])
        del d2

        ans = []
        for el in set(nums1) & set(nums2):
            ans += [el for _ in range(d1[el])]

        return ans


if __name__ == '__main__':
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    sol = Solution()
    print(sol.intersect(nums1, nums2))