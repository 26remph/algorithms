dig = input()

p1 = p2 = p3 = p4 = p5 = p6 = dig[0] + dig[1]

if dig[0] != '0':

    p1 = dig[0] + dig[1]
    p2 = dig[0] + dig[2]

if dig[1] != '0':
    p3 = dig[1] + dig[0]
    p4 = dig[1] + dig[2]

if dig[2] != '0':
    p5 = dig[2] + dig[0]
    p6 = dig[2] + dig[1]

print(min(p1, p2, p3, p4, p5, p6), max(p1, p2, p3, p4, p5, p6))
