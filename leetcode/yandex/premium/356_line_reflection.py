from typing import List


# Formatted question description: https://leetcode.ca/all/356.html
# Given n points on a 2D plane, find if there is such a line parallel
# to the y-axis that reflects the given points symmetrically.
# In other words, answer whether or not if there exists a line that after reflecting
# all points over the given line, the original points'
# set is the same as the reflected ones.
# Note that there can be repeated points.


class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        dots = {(x, y) for x, y in points}
        line_x = min(points)[0] + max(points)[0]
        for i, j in points:
            if (line_x - i, j) not in dots:
                return False
        return True

    def way1_isReflected(self, points: List[List[int]]) -> bool:
        min_x, max_x = float("inf"), float("-inf")
        point_set = set()
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))
        s = min_x + max_x
        for x, y in points:
            if (s - x, y) not in point_set:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isReflected())
