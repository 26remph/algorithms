s1, s2, s3 = input(), input(), input()
const = 'зайка'

rez = ''
if const in s1:
    if not rez or len(s1) < len(rez):
        rez = s1

if const in s2:
    if not rez or s2 < rez:
        rez = s2

if const in s3:
    if not rez or s3 < rez:
        rez = s3

print(rez, len(rez))
