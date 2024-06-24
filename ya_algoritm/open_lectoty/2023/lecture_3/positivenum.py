n = int(input())
arr = list(map(int, input().split()))
pref = [0 for _ in range(len(arr) + 1)]

for i in range(len(arr)):
    if arr[i] >= 0:
        pref[i + 1] += pref[i] + 1
    else:
        pref[i + 1] = pref[i]

q = int(input())
for _ in range(q):
    lo, hi = map(int, input().split())
    print(pref[hi] - pref[lo - 1])
