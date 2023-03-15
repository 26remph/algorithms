from collections import Counter
import time
from string import ascii_lowercase

k = int(input())
s = input()

t = time.time()
if k >= len(s):
    print(len(s))
elif k == 0:
    print(Counter(s).most_common(1)[0][1])

# chars = set(s)
chars = [-1] * (ord(ascii_lowercase[-1]) + 1)
for i in range(len(s)):
    if chars[ord(s[i])] == -1:
        chars[ord(s[i])] = i

gmax = 0
# for ch in chars:
for ind in range(len(chars)):
    if chars[ind] == -1:
        continue

    ch = chr(ind)
    pos = chars[ind]
    # i, j = 0, 0
    i, j = pos, pos
    cnt = 0
    # skip = True
    while i < len(s):

        # if skip:
        #     t = time.time()
        #     for i in range(len(s)):
        #         if s[i] != ch:
        #             continue
        #         break
        #     skip = False
        #     i =
        #     j = i
        #
        #     print('skip time(s):', time.time() - t)

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
print('time(s):', time.time() - t)
