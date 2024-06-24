from bisect import bisect_left, bisect_right


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

x_ind = sorted(arr, key=lambda x: (x[0], x[1]))
x_keys = [x[0] for x in x_ind]
_sum, x_sum = 0, []
for row in x_ind:
    _sum += row[2]
    x_sum.append(_sum)

y_ind = sorted(arr, key=lambda x: (x[1], x[0]))
y_keys = [x[1] for x in y_ind]
_sum, y_sum = 0, []
for row in y_ind:
    _sum += row[1] - row[0]
    y_sum.append(_sum)

q = int(input())
out = []
for _ in range(q):
    row = list(map(int, input().split()))
    start, end, q_type = row

    if q_type == 2:
        src, search_key, keys, total = y_ind, 1, y_keys, y_sum
    else:
        src, search_key, keys, total = x_ind, 0, x_keys, x_sum

    right = bisect_right(keys, end)
    if right:
        right -= 1
    left = bisect_left(keys, start)

    _sum = 0
    if left <= right and len(src) == 1:
        if src[0][search_key] <= end:
            _sum = total[0]

    if left <= right and len(src) > 1:
        if left - 1 < 0:
            if src[right][search_key] <= end:
                _sum = total[right]
        else:
            _sum = total[right] - total[left - 1]

    out.append(str(_sum))

print(' '.join(out))
