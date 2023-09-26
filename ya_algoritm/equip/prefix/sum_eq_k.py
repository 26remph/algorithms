import collections


def subarray_sum(nums, k):
    """Prefix sum for array with negative integer numbers"""
    ans = 0
    total = 0
    prefix_summ = collections.defaultdict(int)
    prefix_summ[0] = 1  # for case total equal k
    for n in nums:
        total += n
        prefix = total - k
        ans += prefix_summ.get(prefix, 0)
        prefix[total] += 1

    return ans
