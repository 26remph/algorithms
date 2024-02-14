fn = 'q1.txt'
ans = []
with open(fn, encoding='UTF-8') as f:
    while ch := f.read(1):
        start = len(bin(ord(ch))[2:]) % 8
        encode_ch = bin(ord(ch))[2 + start:] if ord(ch) > 127 else bin(ord(ch))

        ans.append(chr(int(encode_ch, 2)))

print(''.join(ans))