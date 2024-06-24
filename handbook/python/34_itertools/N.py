import itertools


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr.sort()

for s in itertools.permutations(arr, 3):
    print(', '.join(s))
