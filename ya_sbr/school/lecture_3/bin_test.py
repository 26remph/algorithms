def bin_search(arr, x, lo, hi):

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            hi = mid
        else:
            lo = mid + 1

    return lo


arr = [15, 15, 15, 15, 14, 14, 13, 12, 12, 10, 9, 8, 6, 6, 4, 3, 2, 1, 1, 0, 0]

k = 5
ind = bin_search(arr, k, 0, len(arr))
print('ind', ind, 'k', k)
