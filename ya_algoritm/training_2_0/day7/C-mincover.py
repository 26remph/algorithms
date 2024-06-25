M = int(input())

OPEN = 1
SEPARATOR = 0
CLOSE = -1

L = (0, SEPARATOR, M)
R = (M, SEPARATOR, 0)
arr = [L, R]
while (row := input()) != '0 0':
    start, end = map(int, row.split())
    arr.append((start, OPEN, end))
    arr.append((end, CLOSE, start))

arr.sort(key=lambda x: (x[0], x[1]))
print(arr)

cnt = 0
cnt_arr = [0] * len(arr)
indL, indR = 0, 0
for i in range(len(arr)):
    if arr[i] == L:
        indL = i
    elif arr[i] == R:
        indR = i

    if arr[i][1] == OPEN:
        cnt += 1
        cnt_arr[i] = cnt
    elif arr[i][1] == CLOSE:
        cnt -= 1
        cnt_arr[i] = cnt
    else:
        cnt_arr[i] = cnt


print(cnt_arr)
print(indL, indR)
cover_cnt = cnt_arr[indL + 1: indR]
print('cover_cnt:', cover_cnt)

min_cnt = 0
if cover_cnt:
    min_cnt = min(cover_cnt[:-1]) if len(cover_cnt) > 1 else cover_cnt[0]

if not min_cnt:
    print('No solution')
else:
    print(min_cnt)
    ans = set()
    for i in range(indL + 1, indR):
        if arr[i][1] == OPEN:
            # print(arr[i][0], arr[i][2])
            ans.add((arr[i][0], arr[i][2]))
        else:
            ans.add((arr[i][2], arr[i][0]))
            # print(arr[i][2], arr[i][1])

    for cut in sorted(ans):
        print(cut[0], cut[1])
