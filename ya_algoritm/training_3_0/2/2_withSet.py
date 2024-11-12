import time

from collections import Counter


k = int(input())
s = input()

t = time.time()
# chars = set(s)
chars = set()
chars.add("l")

if k >= len(s):
    print(len(s))
elif k == 0:
    print(Counter(s).most_common(1)[0][1])

gmax = 0
for ch in chars:
    i, j = 0, 0
    cnt = 0
    skip = True
    while i < len(s):
        if skip:
            for i in range(len(s)):
                if s[i] != ch:
                    continue
                break
            skip = False
            j = i

        cnt += 1 if ch != s[i] else 0
        cnt -= 1 if j < i and ch != s[j - 1] else 0

        while i < len(s) - 1 and cnt <= k:
            if cnt == k and s[i + 1] != ch:
                break

            i += 1

            if ch != s[i]:
                cnt += 1

        i += 1
        j += 1

    ans = max(i - j + 1, k + 1)
    gmax = max(gmax, ans)

print(gmax)
print("time(s):", time.time() - t)
