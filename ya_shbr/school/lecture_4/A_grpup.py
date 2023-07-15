N = int(input())
group = list(map(int, input().strip().split()))
M = int(input())
room = list(map(int, input().strip().split()))

room.sort(reverse=True)
group.sort(reverse=True)

j = 0
col = 0
for i in range(M):
    while j < N:
        if room[i] >= group[j]:
            col += 1
            j += 1
            break

        j += 1

print(col)
