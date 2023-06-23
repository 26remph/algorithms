from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = defaultdict(list, [])


for i in range(n):
    cnt[arr[i]].append(i)

ans = 'NO'
for i in range(n):
    if len(cnt[arr[i]]) > 1:
        pos = cnt[arr[i]]

        if min([pos[j] - pos[j-1] for j in range(1, len(pos))]) <= k:
            ans = 'YES'
            break
print(ans)


