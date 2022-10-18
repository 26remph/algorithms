import string

abc = string.ascii_lowercase

n = input()
for _ in range(int(n)):

    data = input().split(',')

    fio = ''.join(data[:3])
    diff_ch = len(set(fio))
    birth = ''.join(data[3:-1])
    birth_code = 0
    for ch in birth:
        birth_code += int(ch)

    birth_code *= 64
    ch_code = abc.find(fio[0].lower()) + 1
    ch_code *= 256

    code = diff_ch + birth_code + ch_code
    rez = str(hex(code))[-3:]
    if len(rez) < 3:
        rez.rjust(3 - len(rez), '0')

    print(rez.upper())

