import itertools

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr.sort()
for s in itertools.permutations(arr):
    print(', '.join(s))
