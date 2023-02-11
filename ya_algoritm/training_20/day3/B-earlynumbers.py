nums = list(map(int, input().split()))
early_nums = set()

for i in range(len(nums)):
    if nums[i] not in early_nums:
        early_nums.add(nums[i])
        print('NO')
    else:
        print('YES')

