# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:

    # versions = [False, False, False, True, True]
    # versions = [True]
    versions = [False, False, False, False, False, False, False, True]
    print(versions)
    return versions[version - 1]


class Solution:
    def firstBadVersion(self, n: int) -> int:

        lo, hi = 1, n

        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
            # print(lo, hi, mid)

        # print(lo)
        return lo
        # print(lo, hi, mid)


sol = Solution()
sol.firstBadVersion(8)