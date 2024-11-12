import sys

from collections import Counter


cnt = Counter()

while row := sys.stdin.readline():
    if not cnt:
        cnt = Counter(row.rstrip())
    else:
        cnt.update(Counter(row.rstrip()))


# for row in sys.stdin:
#     if not cnt:
#         cnt = Counter(row.strip())
#     else:
#         cnt.update(Counter(row.strip()))

if cnt.get(" "):
    cnt.pop(" ")

lst = cnt.most_common()
max_val = -1 if not lst else lst[0][1]

lst.sort(key=lambda x: ord(x[0]))
for lvl in range(max_val, 0, -1):
    chars = []
    for ind in range(len(lst)):
        if lst[ind][1] == lvl:
            chars.append("#")
            lst[ind] = (lst[ind][0], lst[ind][1] - 1)
        else:
            chars.append(" ")

    print("".join(chars))

print("".join([x[0] for x in lst]))
