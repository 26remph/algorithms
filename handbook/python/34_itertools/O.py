import itertools


n = int(input())
arr = []
for _ in range(n):
    arr += input().split(", ")
arr.sort()
for lst in itertools.permutations(arr, 3):
    print(" ".join(lst))
