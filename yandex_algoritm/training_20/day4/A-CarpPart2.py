N = int(input())

ans = {}
for _ in range(N):
    key, value = map(int, input().split())
    if ans.get(key):
        ans[key] += value
    else:
        ans[key] = value

for key in sorted(ans.keys()):
    print(f'{key} {ans[key]}')
