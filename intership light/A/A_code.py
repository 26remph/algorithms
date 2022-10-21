import string

abc = string.ascii_lowercase

n = input()
out = []
for _ in range(int(n)):

    arr = input().split(',')

    fio = ''.join(arr[:3])
    first_code = len(set(fio))
    birth = ''.join(arr[3:-1])
    second_code = 0
    for ch in birth:
        second_code += int(ch)

    second_code *= 64
    third_code = abc.find(fio[0].lower()) + 1
    third_code *= 256

    code = first_code + second_code + third_code
    code_out = str(hex(code))[-3:]
    if len(code_out) < 3:
        code_out.rjust(3 - len(code_out), '0')

    out.append(code_out.upper())

print(' '.join(out))