import collections
import heapq
from pprint import pprint
from typing import List


class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        d = [[] for _ in range(n + m)]
        for i in range(n):
            for j in range(m):
                heapq.heappush(d[i-j], mat[i][j])

        for i in range(n):
            for j in range(m):
                mat[i][j] = heapq.heappop(d[i-j])

        return mat

    def arr_diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])

        # pprint(d)

        for v in d.values():
            v.sort(reverse=True)

        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i-j].pop()

        return mat


if __name__ == '__main__':
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    out = [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    sol = Solution()
    print(sol.diagonalSort(mat))

