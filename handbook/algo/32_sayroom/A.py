n = int(input())
cuts = []
for _ in range(n):
    cuts.append(tuple(map(int, input().split())))
cuts.sort(key=lambda x: x[1])
cur = cuts[0]
ans = [cur]
for cut in cuts:

    if cut[0] <= cur[1]:
        continue
    else:
        cur = cut
        ans.append(cur)

print(len(ans))