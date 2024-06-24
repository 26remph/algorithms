import string

from collections import Counter


def prettyfor(k, s):

    chars = set(s)
    # chars = 'a'

    if k >= len(s):
        return len(s)
    elif k == 0:
        return Counter(s).most_common(1)[0][1]

    gmax = 0
    for ch in chars:

        summa = 0
        cnt_z = 0
        left_summa = 0
        r_summa = 0
        skip = True
        for i in range(len(s)):
            if s[i] != ch and skip:
                continue

            skip = False

            if s[i] == ch:
                summa += 1
                r_summa += 1 if cnt_z >= 1 else 0
                # print('i', i, 'summa-ch', summa, 'r_summa-ch', r_summa)
            else:
                cnt_z += 1
                if cnt_z == k:
                    left_summa = summa - k + 1
                    # print('SAVE')
                    # print('i', i, 'l_sum=', left_summa, 'r_summa=', r_summa,
                    #       'sum=', summa, 'cnt_z=', cnt_z)

                if cnt_z > k:
                    summa = summa - left_summa - k
                    if summa == 0:
                        left_summa = r_summa - 1
                        summa = left_summa
                        cnt_z = k
                        r_summa = 0
                    elif summa > 0:
                        left_summa = summa
                        cnt_z = 1
                        r_summa = 0
                    elif summa < 0:
                        summa = k - 1
                        left_summa = summa
                        cnt_z = k
                        r_summa = 0
                    # print('RESET')
                    # print('i', i, 'gmax=', gmax, 'l_sum=', left_summa,
                    #       'r_summa', r_summa, 'sum=', summa, 'cnt_z', cnt_z)

                summa += 1
                r_summa += 1 if cnt_z >= 1 else 0
                # print('i', i, 'summa-dot', summa, 'r_summa-dot', r_summa)

            gmax = max(gmax, summa)

        # print('ch', ch, 'gmax', gmax)
        # print('ch', ch, 'summa', summa, 'left_summa=', left_summa, 'r_summa', r_summa)

    return gmax


if __name__ == '__main__':

    # k = int(input())
    # s = input()
    #
    # t = time.time()
    # print(prettyfor(k, s))
    # print('(s):', time.time() - t)
    k = 7
    s = 'ubejxxiazk'
    assert (rez := prettyfor(k, s)) == 9, f'{rez}, s={s}, k={k}'

    k = 7
    s = 'ubejxxxazk'
    assert (rez := prettyfor(k, s)) == 10, f'{rez}, s={s}, k={k}'

    k = 7
    s = 'ubejxxxxzk'
    assert (rez := prettyfor(k, s)) == 10, f'{rez}, s={s}, k={k}'

    k = 7
    s = 'adubejqwvxk'
    assert (rez := prettyfor(k, s)) == 8, f'{rez}, s={s}, k={k}'

    k = 5
    s = 'abcdefxxgh'
    assert (rez := prettyfor(k, s)) == 7, f'{rez}, s={s}, k={k}'

    k = 25
    s = 'dlfbsgiclfthywlnniyzsrbmmbjsdhdulbumeyumuobdekoguq'
    assert (rez := prettyfor(k, s)) == 30, f'{rez}, s={s}, k={k}'

    k = 50
    s = 'pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh'  # noqa: E501
    assert (rez := prettyfor(k, s)) == 57, f'{rez}, s={s}, k={k}'

    k = 10
    s = 'oatairvumfhblqdtnquivtriihsixp'
    assert (rez := prettyfor(k, s)) == 14, f'{rez}, s={s}, k={k}'

    k = 25
    s = 'dlfbsgiclfthywlnniyzsrbmmbjsdhdulbumeyumuobdekoguq'
    assert (rez := prettyfor(k, s)) == 29, f'{rez}, s={s}, k={k}'

    k = 50
    s = 'pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh'  # noqa: E501
    assert (rez := prettyfor(k, s)) == 57, f'{rez}, s={s}, k={k}'

    k = 4
    s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
    assert (rez := prettyfor(k, s)) == 20, f'{rez}, s={s}, k={k}'

    k = 4
    s = 'abcdeaaafaaaaaagxlmnaaaaaaaaaaa'
    assert (rez := prettyfor(k, s)) == 15, f'{rez}, s={s}, k={k}'

    k = 4
    s = 'abcdeaaafaaaaaagxlmnaaaaaaaa'
    assert (rez := prettyfor(k, s)) == 13, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
    assert (rez := prettyfor(k, s)) == 11, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'a'
    assert (rez := prettyfor(k, s)) == 1, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'abcdefg'
    assert (rez := prettyfor(k, s)) == 2, f'{rez}, s={s}, k={k}'

    k = 1
    s = string.ascii_lowercase
    assert (rez := prettyfor(k, s)) == 2, f'{rez}, s={s}, k={k}'

    k = 2
    s = 'abcaz'
    assert (rez := prettyfor(k, s)) == 4, f'{rez}, s={s}, k={k}'

    k = 2
    s = 'helto'
    assert (rez := prettyfor(k, s)) == 3, f'{rez}, s={s}, k={k}'

    k = 5
    s = 'helto'
    assert (rez := prettyfor(k, s)) == 5, f'{rez}, s={s}, k={k}'
    #
    k = 6
    s = 'helto'
    assert (rez := prettyfor(k, s)) == 5, f'{rez}, s={s}, k={k}'

    k = 3
    s = 'helto'
    assert (rez := prettyfor(k, s)) == 4, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'acaaa'
    assert (rez := prettyfor(k, s)) == 5, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'acdaaad'
    assert (rez := prettyfor(k, s)) == 4, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'acdaaa'
    assert (rez := prettyfor(k, s)) == 4, f'{rez}, s={s}, k={k}'

    k = 1
    s = 'aaaabbbb'
    assert (rez := prettyfor(k, s)) == 5, f'{rez}, s={s}, k={k}'

    k = 0
    s = 'aaaabbbb'
    assert (rez := prettyfor(k, s)) == 4, f'{rez}, s={s}, k={k}'

    k = 0
    s = 'a'
    assert (rez := prettyfor(k, s)) == 1, f'{rez}, s={s}, k={k}'

    k = 0
    s = 'abbbbbb'
    assert (rez := prettyfor(k, s)) == 6, f'{rez}, s={s}, k={k}'

    k = 3
    s = 'aaaaaaaa'
    assert (rez := prettyfor(k, s)) == 8, f'{rez}, s={s}, k={k}'
