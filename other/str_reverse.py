# s = 'BigCat'
# print(''.join(reversed(s)).capitalize())

s = 'BigCat'
i, j = 0, len(s) - 1
rez = ['_'] * len(s)
while i < j:
    rez[j], rez[j] = s[i], s[j]
    i += 1
    j -= 1

print(''.join(rez).capitalize())

s = 'BigCat'
print(s[::-1].capitalize())

S = 'BigCat'
print(S[::2])
print(S[0:1])
R = '[] U [)'

s = 'BigCat'
row = s[-1] + s[-2] + s[-3] + s[-4] + s[-5] + s[-6]
print(row.capitalize())



