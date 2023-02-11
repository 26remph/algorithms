nums = list(map(int, input().split()))

unique = set(nums)
not_unique = set()

for num in nums:
    if num in unique:
        unique.remove(num)
    else:
        not_unique.add(num)

ans = []
for num in nums:
    if num not in not_unique:
        ans.append(str(num))

print(' '.join(ans))

