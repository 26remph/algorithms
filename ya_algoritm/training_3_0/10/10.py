from collections import Counter


s = input()
count = Counter()

for i in range(len(s)):
    cnt = (i + 1) * (len(s) - i)
    count.update({s[i]: cnt})

ans = count.most_common()
ans.sort(key=lambda x: x[0])

for val in ans:
    print(f"{val[0]}: {val[1]}")
