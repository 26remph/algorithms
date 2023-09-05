s = ''.join(input().lower().split())
flag = True
for i in range(len(s) // 2):

    if s[i] != s[len(s) - i - 1]:
        flag = False
        break

print('YES' if flag else 'NO')



