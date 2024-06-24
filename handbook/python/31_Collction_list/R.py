s = input()

ch = s[0]
cnt = 0

for i in range(len(s)):

    if s[i] == ch:
        cnt += 1
    else:
        print(ch, cnt)
        ch = s[i]
        cnt = 1

print(ch, cnt)
