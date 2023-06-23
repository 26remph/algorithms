# n = int(input())
# arr = list(map(int, input().split()))
import random

replay = 0
while (replay:= replay + 1) != 10_000:
    n = random.randint(1, 100)
    arr = []
    for _ in range(n):
        arr.append(random.randint(1, 10))

    arr.sort()
    num = arr[0]
    maxseq = 0
    cur, total_cur = 0, 0
    for i in range(n):

        if arr[i] == num:
            cur += 1
            total_cur += 1
        elif arr[i] - num <= 1:
            total_cur += 1
        else:
            maxseq = max(maxseq, total_cur)
            total_cur = total_cur - cur
            num = arr[i - total_cur]
            # print("num:", num, 'i:', i)
            # print('cur:', cur, 'total:', total_cur)
            total_cur += 1
            cur = 1


    maxseq = max(maxseq, total_cur)
    # print(len(arr) - maxseq)
    ans = len(arr) - maxseq

    col = 0
    max_col = 0
    for i in range(n):
        for j in range(i, n):
            if arr[j] - arr[i] <= 1:
                col += 1
        max_col = max(max_col, col)
        col = 0
    # print(len(arr) - max_col)
    ans_1 = len(arr) - max_col

    assert ans_1 == ans, print(' '.join(map(str, arr)))
print('ok', replay, '(pass)')

