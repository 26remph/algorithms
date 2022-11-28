# sentinel = ''
# ends when this string is seen
# for line in iter(input, sentinel):
#     pass

# ans = {}
# while row := input():
# for row in iter(input, sentinel):
#
#     key, val = row.split()
#     val = int(val)
#     if ans.get(key):
#         ans[key] += val
#     else:
#         ans[key] = val

# for key in sorted(ans.keys()):
#     print(key, ans[key])

# import sys
# ans = {}
# while row := sys.stdin.readline().strip():
#     # print(row)
#     key, val = row.split()
#     val = int(val)
#     if ans.get(key):
#         ans[key] += val
#     else:
#         ans[key] = val
#
# for key in sorted(ans.keys()):
#     print(key, ans[key])

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
