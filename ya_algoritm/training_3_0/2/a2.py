# k = int(input())
# s = input()

s = '0000111101110111111'

summa = 0
cnt_z = 0
left_summa = 0
gsumm = 0
skip = True
for i in range(len(s)):
    if s[i] == '0' and skip:
        continue

    skip = False

    if s[i] == '1':
        summa += 1
    else:
        cnt_z += 1

        if cnt_z == 1:
            left_summa = summa

        if cnt_z >= 2:
            gsumm = max(gsumm, summa)
            summa = summa - left_summa
            cnt_z = 1
        else:
            summa += 1

gsumm = max(gsumm, summa)

print('gsumm', gsumm)
