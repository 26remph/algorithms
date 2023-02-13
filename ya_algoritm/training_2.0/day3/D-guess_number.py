N = int(input())
nums = set(range(1, N + 1))
while (row := str(input())) != 'HELP':
    query_nums = set(map(int, row.split()))
    Q = input()
    if Q == 'YES':
        nums.intersection_update(query_nums)
    else:
        nums.difference_update(query_nums)

print(' '.join(list(map(str, sorted(nums)))))
