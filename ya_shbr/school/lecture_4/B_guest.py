N = int(input())
cuts = []
for ind in range(N):
    a, b = map(int, input().strip().split())
    cuts.append((a, b, ind))

cuts.sort(key=lambda x: x[0])

ans = [cuts[0]]
t = cuts[0][1]

for i in range(1, len(cuts)):
    if cuts[i][1] <= t:
        ans.append((-1, -1, cuts[i][2]))
        continue

    if cuts[i][1] > t:
        ans.append((max(t, cuts[i][0]), cuts[i][1], cuts[i][2]))

    t = cuts[i][1]

ans.sort(key=lambda x: x[2])

for x in ans:
    print(x[0], x[1])

# print('cuts:', cuts)
# print('ans:', ans)



