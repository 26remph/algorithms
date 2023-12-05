col_num = 0
col_positive = 0
min_num = float("inf")
max_num = float("-inf")
total = 0
avg = 0

with open(input(), encoding="UTF-8") as f:
    for line in f:
        arr = list(map(int, line.split()))
        col_num += len(arr)
        col_positive += sum([1 for x in arr if x > 0])
        min_num = min(min_num, min(arr))
        max_num = max(max_num, max(arr))
        total += sum(arr)

avg = total / col_num
print(col_num)
print(col_positive)
print(min_num)
print(max_num)
print(total)
print(f'{avg:.3}')


