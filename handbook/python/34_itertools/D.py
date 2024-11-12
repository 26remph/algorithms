from itertools import accumulate


arr = input().split()
for val in accumulate(arr, lambda x, y: f"{x} {y}"):
    print(val)
