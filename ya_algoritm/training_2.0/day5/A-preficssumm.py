N, Q = map(int, input().split())
arr = list(map(int, input().split()))
pref = [0]*(N+1)
for i in range(len(arr)):
    pref[i+1] = pref[i]+arr[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(pref[R]-pref[L-1])



