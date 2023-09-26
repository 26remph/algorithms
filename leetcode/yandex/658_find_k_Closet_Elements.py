from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        i = 0
        ind = 0
        while i < len(arr):
            if abs(arr[ind] - x) > (arr[i] - x):
                ind = i
            i += 1

        res = []
        res.append(arr[ind])
        print(f'{res=}')
        j = ind + 1
        i = ind - 1
        while i >= 0 and j < len(arr):

            if len(res) == k:
                break

            if abs(arr[i] - x) < abs(arr[j] - x) or (abs(arr[i] - x) == abs(arr[j] - x) and arr[i] < arr[j]):
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1

        while i >= 0 and len(res) < k:
            res.append(arr[i])
            i -= 1

        while j < len(arr) and len(res) < k:
            res.append(arr[j])
            j += 1

        res.sort()
        return res


if __name__ == '__main__':
    tests = (
        ([1,3], 1, 2, [1]),
        ([0,0,1,2,3,3,4,7,7,8], 3, 5, [3,3,4]),
        ([1,2,3,4,5], 4, 3, [1,2,3,4]),
        ([1,2,3,4,5], 4, -1, [1,2,3,4]),
        ([1,1,1,10,10,10], 1, 9, [10]),
    )
    sol = Solution()
    for a, k, x, ans in tests:
        res = sol.findClosestElements(a, k, x)
        assert ans == res, f'{k=}, {x=}, {a=}, {res=}'