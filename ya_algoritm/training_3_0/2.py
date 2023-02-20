# k = int(input())
# s = input()
import string
from collections import Counter


def pretty(k, s):

    chars = set(s)

    if k >= len(s):
        return len(s)
    elif k == 0:
        return Counter(s).most_common(1)[0][1]

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
            cnt -= 1 if ch != s[j] else 0

            while cnt <= k and i < len(s) - 1:
                i += 1
                if ch != s[i]:
                    cnt += 1
            else:
                i += 1
                j += 1

        ans = max(i - j, k + 1)
        gmax = max(gmax, ans)

    return gmax


k = 50
s = 'pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh'
assert (rez := pretty(k, s)) == 57, f'{rez}, s={s}, k={k}'

k = 4
s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
assert (rez := pretty(k, s)) == 20, f'{rez}, s={s}, k={k}'

k = 4
s = 'abcdeaaafaaaaaagxlmnaaaaaaaaaaa'
assert (rez := pretty(k, s)) == 15, f'{rez}, s={s}, k={k}'

# k = 4
# s = 'abcdeaaafaaaaaagxlmnaaaaaaaa'
# assert (rez := pretty(k, s)) == 13, f'{rez}, s={s}, k={k}'


k = 1
s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
assert (rez := pretty(k, s)) == 11, f'{rez}, s={s}, k={k}'

k = 1
s = 'a'
assert (rez := pretty(k, s)) == 1, f'{rez}, s={s}, k={k}'

k = 1
s = 'abcdefg'
assert (rez := pretty(k, s)) == 2, f'{rez}, s={s}, k={k}'

k = 1
s = string.ascii_lowercase
assert (rez := pretty(k, s)) == 2, f'{rez}, s={s}, k={k}'

k = 2
s = 'abcaz'
assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

k = 2
s = 'helto'
assert (rez := pretty(k, s)) == 3,f'{rez}, s={s}, k={k}'

k = 5
s = 'helto'
assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

k = 6
s = 'helto'
assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

k = 3
s = 'helto'
assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

k = 1
s = 'acaaa'
assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

k = 1
s = 'acdaaad'
assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

k = 1
s = 'acdaaa'
assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

k = 1
s = 'aaaabbbb'
assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

k = 0
s = 'aaaabbbb'
assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

k = 0
s = 'a'
assert (rez := pretty(k, s)) == 1, f'{rez}, s={s}, k={k}'

k = 0
s = 'abbbbbb'
assert (rez := pretty(k, s)) == 6, f'{rez}, s={s}, k={k}'

