N = int(input())

OPEN = 1
CLOSE = -1

arr = []
for _ in range(N):
    start, duration = map(int, input().split())
    end = start + duration
    arr.append((start, OPEN))
    arr.append((end, CLOSE))

arr.sort(key=lambda x: (x[0], x[1] == OPEN))
# print(arr)
cnt = 0
max_cnt = 0
for act in arr:
    cnt += act[1]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
