from collections import defaultdict


def gcd(a, b):
    while b:
        a %= b
        a, b = b, a

    return a


nums = defaultdict(list)
arr = list(set((map(int, input().split("; ")))))
arr.sort()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        a, b = arr[i], arr[j]
        if gcd(b, a) == 1:
            nums[a].append(b)
            nums[b].append(a)

for key, val in sorted(list(nums.items())):
    print(key, "-", ", ".join(map(str, val)))
