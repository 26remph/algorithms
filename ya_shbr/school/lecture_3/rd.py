import bisect
import itertools


arr = [-5, -2, 1, 2, 3]
arr.sort()

ind = bisect.bisect_right(arr, 3)
print(ind, arr)

