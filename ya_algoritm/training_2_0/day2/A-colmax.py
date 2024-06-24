
maxN = 0
seq = []

while (n := int(input())) != 0:
    maxN = max(maxN, n)
    seq.append(n)

cnt = sum([1 for x in seq if x == maxN])
print(cnt)
