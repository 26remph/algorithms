import collections
from typing import List




class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid), len(grid[0])
        visited = [0] * (n * m)

        stack = collections.deque()
        island = 0
        for dot in range(len(visited)):

            if not visited[dot]:
                i, j = dot // m, dot % m

                visited[dot] = 1
                if grid[i][j] == "1":
                    stack.append((i, j))
                    while stack:
                        i, j = stack.popleft()
                        l = (i, j-1) if j - 1 >= 0 and grid[i][j-1] == '1' else None
                        r = (i, j+1) if j + 1 < m and grid[i][j+1] == '1' else None
                        u = (i-1, j) if i - 1 >= 0 and grid[i-1][j] == '1' else None
                        d = (i+1, j) if i + 1 < n and grid[i+1][j] == '1' else None
                        for p in (l, r, u, d):
                            if p:
                                if not visited[p[0] * m + p[1]]:
                                    visited[p[0] * m + p[1]] = 1
                                    print(f'dot={p[0] * m + p[1]}, {p[0], p[1]}')
                                    stack.append(p)
                    island += 1
                    print(visited)
        return island


if __name__ == '__main__':
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    sol = Solution()
    ans = sol.numIslands(grid)
    print(ans)