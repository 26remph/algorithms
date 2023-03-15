from collections import Counter

k = int(input())
s = input()

chars = Counter(s).most_common()
max_freq = chars[0][1]

if k >= len(s):
    print(len(s))
elif k == 0:
    print(max_freq)

gmax = 0
for ch, freq in chars:

    if freq < max_freq and max_freq >= k:
        break

    i, j = 0, 0
    cnt = 0
    while i < len(s):

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

if k < len(s):
    print(gmax)

