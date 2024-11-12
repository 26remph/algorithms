from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        last = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue
            else:
                res.append(
                    f"{last}->{nums[i - 1]}" if last != nums[i - 1] else str(last)
                )
                last = nums[i]

        res.append(f"{last}->{nums[-1]}" if last != nums[-1] else str(last))

        return res


if __name__ == "__main__":
    test = (
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    )

    sol = Solution()
    for arr, ans in test:
        res = sol.summaryRanges(arr)
        assert res == ans, f"{ans=}, {res=}, {arr=}"
