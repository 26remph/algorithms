# k = int(input())
# s = input()

# k = 1
# s = '0000111101110111111'
# ch = '1'
# ans = 10

# k = 1
# s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
# ch = 'a'
# assert (rez := pretty(k, s)) == 11, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'a'
# ch = 'a'
# assert (rez := pretty(k, s)) == 1, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'abcdefg'
# ch = 'a'
# assert (rez := pretty(k, s)) == 2, f'{rez}, s={s}, k={k}'

# k = 1
# s = string.ascii_lowercase
# ch = 'a'
# assert (rez := pretty(k, s)) == 2, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'acaaa'
# ch = 'a'
# assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'acdaaad'
# ch = 'a'
# assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'acdaaa'
# ch = 'a'
# assert (rez := pretty(k, s)) == 4, f'{rez}, s={s}, k={k}'

# k = 1
# s = 'aaaabbbb'
# ch = 'a'
# assert (rez := pretty(k, s)) == 5, f'{rez}, s={s}, k={k}'

# k = 2
# s = '0000111101110111111'
# ch = '1'
# 15

# k = 4
# s = 'abcdeaaafaaaaaagxlmaaaaaaaaaa'
# ch = 'a'
# assert (rez := pretty(k, s)) == 20, f'{rez}, s={s}, k={k}'

# k = 4
# s = 'aaafaaaaaagxlmaaaaaaaaaa'
# ch = 'a'
# 20

# k = 4
# s = 'aaaaaagxlmaaaaaaaaaa'
# ch = 'a'
# ans = 20

# k = 4
# s = 'abcdeaaafaaaaaagxlmnaaaaaaaaaaa'
# ch = 'a'
# assert (rez := pretty(k, s)) == 15, f'{rez}, s={s}, k={k}'

# k = 50
# s = 'pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh'  # noqa: E501
# ch = 'g'
# 57

# k = 5
# s = 'pnwkegzullrzknjlgqtelcnzdogghzoecjvpafekvllwijezhhh'
# ch = 'g'

# k = 10
# s = 'oatairvumfhblqdtnquivtriihsixp'
# ch = 'i'

k = 10
s = "irvumfhblqdtnquivtriihsixp"
ch = "i"


summa = 0
cnt_z = 0
left_summa = 0
gsumm = 0
r_summa = 0
skip = True
for i in range(len(s)):
    if s[i] != ch and skip:
        continue

    skip = False

    if s[i] == ch:
        summa += 1
        r_summa += 1 if cnt_z >= 1 else 0
        print("i", i, "summa-ch", summa, "r_summa-ch", r_summa)
    else:
        cnt_z += 1
        if cnt_z == k:
            left_summa = summa - k + 1
            print("SAVE")
            print(
                "i",
                i,
                "l_sum=",
                left_summa,
                "r_summa=",
                r_summa,
                "sum=",
                summa,
                "cnt_z=",
                cnt_z,
            )

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
            print("RESET")
            print(
                "i",
                i,
                "gsumm=",
                gsumm,
                "l_sum=",
                left_summa,
                "r_summa",
                r_summa,
                "sum=",
                summa,
                "cnt_z",
                cnt_z,
            )

        summa += 1
        r_summa += 1 if cnt_z >= 1 else 0
        print("i", i, "summa-dot", summa, "r_summa-dot", r_summa)

    gsumm = max(gsumm, summa)

print("gsumm", gsumm)
print("summa", summa, "left_summa=", left_summa, "r_summa", r_summa)
