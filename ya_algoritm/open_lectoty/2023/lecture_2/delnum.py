n = int(input())
arr = list(map(int, input().split()))
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
        total_cur += 1
        cur = 1

maxseq = max(maxseq, total_cur)
print(len(arr) - maxseq)
