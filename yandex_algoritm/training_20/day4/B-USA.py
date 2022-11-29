import sys
ans = {}
for row in sys.stdin:
    print(row.strip())
    key, val = row.split()
    val = int(val)
    if ans.get(key):
        ans[key] += val
    else:
        ans[key] = val

for key in sorted(ans.keys()):
    print(key, ans[key])
