N = int(input())

OPEN = 1
CLOSE = -1

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, OPEN))
    arr.append((end, CLOSE))

arr.sort(key=lambda x: (x[0], -x[1] == OPEN))
# print(arr)
cnt = 0
sum_cut = 0
start = 0
for act in arr:
    if cnt > 0:
        long = act[0] - start
        sum_cut += long

    start = act[0]
    cnt += act[1]

print(sum_cut)
