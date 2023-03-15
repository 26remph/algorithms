s = input()

stack = []

ch_open = '([{'
ch_close = ')]}'
pair = {'(': ')', '[': ']', '{': '}'}
isTrue = True
for i in range(len(s)):

    if not (s[i] in ch_open or s[i] in ch_close):
        continue

    if s[i] in ch_open:
        stack.append(s[i])
    else:
        if not stack:
            isTrue = False
            break

        ch = stack.pop()
        if pair.get(ch) != s[i]:
            isTrue = False
            break

if stack:
    isTrue = False

print('yes' if isTrue else 'no')





