import string

from collections import Counter


def prettywhile(k, s):
    chars = set(s)
    # chars = 'x'

    if k >= len(s):
        return len(s)
    elif k == 0:
        return Counter(s).most_common(1)[0][1]

    gmax = 0
    for ch in chars:
        # print('-' * 50)
        i, j = 0, 0
        cnt = 0
        # skip = True
        while i < len(s):
            # if skip:
            #     for i in range(len(s)):
            #         if s[i] != ch:
            #             continue
            #         break
            #     skip = False
            #     j = i

            cnt += 1 if ch != s[i] else 0
            cnt -= 1 if j < i and ch != s[j - 1] else 0
            # print('ch=', ch, 'gcnt=', cnt, 'i,j=', i, j)

            while i < len(s) - 1 and cnt <= k:
                if cnt == k and s[i + 1] != ch:
                    break

                i += 1

                if ch != s[i]:
                    cnt += 1
                # print('wh:', 'ch=', ch, 'cnt =', cnt, 'i,j=', i, j)

            i += 1
            j += 1

        ans = max(i - j + 1, k + 1)
        gmax = max(gmax, ans)
        # print('gl:,', 'ch=', ch, 'cnt =', cnt, 'i,j=', i, j)
        # print('ans=', ans, 'gmax=', gmax)

    return gmax


if __name__ == "__main__":
    # k = int(input())
    # s = input()
    # t = time.time()
    # print(prettywhile(k, s))
    # print('(s):', time.time() - t)
    # assert False

    k = 7
    s = "ubejxxiazk"
    assert (rez := prettywhile(k, s)) == 9, f"{rez}, s={s}, k={k}"

    k = 7
    s = "ubejxxxazk"
    assert (rez := prettywhile(k, s)) == 10, f"{rez}, s={s}, k={k}"

    k = 7
    s = "ubejxxxxzk"
    assert (rez := prettywhile(k, s)) == 10, f"{rez}, s={s}, k={k}"

    k = 7
    s = "adubejqwvxk"
    assert (rez := prettywhile(k, s)) == 8, f"{rez}, s={s}, k={k}"

    k = 5
    s = "abcdefxxgh"
    assert (rez := prettywhile(k, s)) == 7, f"{rez}, s={s}, k={k}"

    k = 25
    s = "dlfbsgiclfthywlnniyzsrbmmbjsdhdulbumeyumuobdekoguq"
    assert (rez := prettywhile(k, s)) == 30, f"{rez}, s={s}, k={k}"

    k = 50
    s = "pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh"  # noqa: E501
    assert (rez := prettywhile(k, s)) == 57, f"{rez}, s={s}, k={k}"

    k = 4
    s = "abcdeaaafaaaaaagxlmaaaaaaaaaa"
    assert (rez := prettywhile(k, s)) == 20, f"{rez}, s={s}, k={k}"

    k = 4
    s = "abcdeaaafaaaaaagxlmnaaaaaaaaaaa"
    assert (rez := prettywhile(k, s)) == 15, f"{rez}, s={s}, k={k}"

    k = 4
    s = "abcdeaaafaaaaaagxlmnaaaaaaaa"
    assert (rez := prettywhile(k, s)) == 13, f"{rez}, s={s}, k={k}"

    k = 1
    s = "abcdeaaafaaaaaagxlmaaaaaaaaaa"
    assert (rez := prettywhile(k, s)) == 11, f"{rez}, s={s}, k={k}"

    k = 1
    s = "a"
    assert (rez := prettywhile(k, s)) == 1, f"{rez}, s={s}, k={k}"

    k = 1
    s = "abcdefg"
    assert (rez := prettywhile(k, s)) == 2, f"{rez}, s={s}, k={k}"

    k = 1
    s = string.ascii_lowercase
    assert (rez := prettywhile(k, s)) == 2, f"{rez}, s={s}, k={k}"

    k = 2
    s = "abcaz"
    assert (rez := prettywhile(k, s)) == 4, f"{rez}, s={s}, k={k}"

    k = 2
    s = "helto"
    assert (rez := prettywhile(k, s)) == 3, f"{rez}, s={s}, k={k}"

    k = 5
    s = "helto"
    assert (rez := prettywhile(k, s)) == 5, f"{rez}, s={s}, k={k}"
    #
    k = 6
    s = "helto"
    assert (rez := prettywhile(k, s)) == 5, f"{rez}, s={s}, k={k}"

    k = 3
    s = "helto"
    assert (rez := prettywhile(k, s)) == 4, f"{rez}, s={s}, k={k}"

    k = 1
    s = "acaaa"
    assert (rez := prettywhile(k, s)) == 5, f"{rez}, s={s}, k={k}"

    k = 1
    s = "acdaaad"
    assert (rez := prettywhile(k, s)) == 4, f"{rez}, s={s}, k={k}"

    k = 1
    s = "acdaaa"
    assert (rez := prettywhile(k, s)) == 4, f"{rez}, s={s}, k={k}"

    k = 1
    s = "aaaabbbb"
    assert (rez := prettywhile(k, s)) == 5, f"{rez}, s={s}, k={k}"

    k = 0
    s = "aaaabbbb"
    assert (rez := prettywhile(k, s)) == 4, f"{rez}, s={s}, k={k}"

    k = 0
    s = "a"
    assert (rez := prettywhile(k, s)) == 1, f"{rez}, s={s}, k={k}"

    k = 0
    s = "abbbbbb"
    assert (rez := prettywhile(k, s)) == 6, f"{rez}, s={s}, k={k}"

    k = 3
    s = "aaaaaaaa"
    assert (rez := prettywhile(k, s)) == 8, f"{rez}, s={s}, k={k}"
