from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candy[i + 1] = candy[i] + 1
        # print(candy)

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                if candy[i - 1] == 1:
                    candy[i - 1] = candy[i] + 1
                else:
                    candy[i - 1] = max(candy[i - 1], candy[i] + 1)

        # print(candy)
        return sum(candy)


if __name__ == '__main__':
    # arr = [1, 2, 2]
    arr = [1, 0, 2]
    # arr = [3, 4, 4, 4, 4, 2, 1]
    sol = Solution()
    print(sol.candy(arr))
