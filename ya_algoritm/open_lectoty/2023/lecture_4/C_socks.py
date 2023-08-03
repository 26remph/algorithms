L, N, M = map(int, input().split())

pref = [0] * (L + 1)
cuts = [0] * (L + 1)
for i in range(N):
    l, r = map(int, input().split())
    cuts[l-1] += 1  # left
    cuts[r] -= 1  # right


for i in range(1, len(pref)):
    pref[i] = pref[i-1] + cuts[i-1]

for _ in range(M):
    m = int(input())
    print(pref[m])

