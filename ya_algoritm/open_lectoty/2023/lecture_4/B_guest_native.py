n = int(input())
friends = []
answer = [(-1, -1) for i in range(n)]

for i in range(n):
    first, last = map(int, input().split())
    friends.append((first, last, i))

friends.sort()

cur_start = 0
cur_end = 0
cur_ind = -1

for x in friends:
    if x[1] > cur_end:
        if cur_ind != -1:
            answer[cur_ind] = (cur_start, min(x[0], cur_end))
        cur_start, cur_end, cur_ind = x

if cur_ind != -1:
    answer[cur_ind] = (cur_start, cur_end)

for i in range(n):
    print(answer[i][0], answer[i][1])
