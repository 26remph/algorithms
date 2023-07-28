import collections

a, b = input(), input()


bull = 0
cow_a = collections.defaultdict(int)
match = set()

min_ab = min((len(a), len(b)))
max_ab = max(len(a), len(b))


for i in range(max_ab):
    if i < min_ab and a[i] == b[i]:
        bull += 1
        match.add(i)
    else:
        cow_a[a[i]] += 1

cow = 0
for i in range(len(b)):
    if i in match:
        continue
    cnt = cow_a.get(b[i], None)
    if cnt is not None and cnt > 0:
        cow_a[b[i]] -= 1
        cow += 1

print(bull)
print(cow)


