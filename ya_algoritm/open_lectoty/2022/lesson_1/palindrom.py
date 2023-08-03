def sol(s):
    if len(s) == 1:
        return ''
    middle = len(s) // 2
    flag = False
    for i in range(middle):
        if s[i] != 'a':
            ans = s[:i] + 'a' + s[i + 1:]
            flag = True
            break
    if flag:
        return ans
    else:
        return s[:-1] + 'b'


poly = input()
rez = ''
if len(poly) > 1:
    for i, ch in enumerate(poly):
        if ch != 'a':
            rez = poly[:i] + 'a' + poly[i + 1:]
            if rez == ''.join(list(reversed(rez))):
                rez = ''
            break

    if not rez:
        rez = poly[:-1] + 'b'

print(rez)
print(sol(poly))

# print(ord('b') + 1)
# print(chr(99))
# assert rez < poly
