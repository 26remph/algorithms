from collections import Counter

str_a: str = input().strip()
str_b: str = input().strip()

f = [val for ind, val in enumerate(str_a) if val != str_b[ind]]
cnt = Counter(f)

rez: str = ""
for ind, ch in enumerate(str_b):
    if ch == str_a[ind]:
        rez += 'P'
        continue

    if cnt[ch] > 0:
        rez += 'S'
        cnt.subtract(ch)
    else:
        rez += 'I'

print(rez)
