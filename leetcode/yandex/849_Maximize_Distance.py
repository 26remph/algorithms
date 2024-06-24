import math

from typing import List


class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        prev = -1
        for i in range(len(seats)):
            if seats[i]:
                cur = i if prev < 0 else (i - prev) // 2
                res = max(res, cur)
                prev = i

        return max(res, len(seats) - prev - 1)

    def _zmaxDistToClosest(self, seats: List[int]) -> int:

        max_dist = 1

        zero = 0
        i = 0
        while seats[i] != 1:
            zero += 1
            i += 1
        max_dist = max(max_dist, zero)

        j = len(seats) - 1
        zero = 0
        while seats[j] != 1:
            zero += 1
            j -= 1
        max_dist = max(max_dist, zero)

        zero = 0
        for i in range(i, j + 1):
            if seats[i] == 1:
                zero = 0
            else:
                zero += 1

            max_dist = max(math.ceil(zero / 2), max_dist)

        return max_dist

    def _maxDistToClosest(self, seats: List[int]) -> int:

        zeros = 0
        max_zeros = 0
        total = sum(seats)
        cnt = 0
        for i in range(len(seats)):

            if seats[i] == 1:

                cnt += 1

                if cnt == 1:
                    max_zeros = max(zeros, max_zeros)
                    if total == 1:
                        max_zeros = max(max_zeros, len(seats) - i - 1)
                elif cnt == total:
                    max_zeros = max(len(seats) - i - 1, max_zeros, zeros // 2 + 1 if zeros % 2 else zeros // 2)
                    break
                else:
                    if zeros % 2:
                        max_zeros = max(zeros // 2 + 1, max_zeros)
                    else:
                        max_zeros = max(zeros // 2, max_zeros)
                # print(f'{zeros=}, {cnt=}, {total=}')
                zeros = 0
            else:
                zeros += 1

        return max_zeros if max_zeros else 1


if __name__ == '__main__':
    tests = (
        ([1, 1, 0, 0, 0, 1, 0], 2),
        ([1, 0, 1], 1),
        ([1, 0, 0, 0, 1, 0, 1], 2),
        ([1, 0, 0, 0], 3),
        ([0, 1], 1),
        ([1, 0, 0, 1, 0, 1, 0, 1], 1),
        ([1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 5),
    )

    sol = Solution()
    for arr, ans in tests:
        res = sol.maxDistToClosest(arr)
        assert ans == res, f'{ans=}, {res=}, {arr=}'
