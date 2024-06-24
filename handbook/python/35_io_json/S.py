import string


fn = 's.txt'
fn_out = 's_out.txt'
shift = int(input())
ans = []
with open(fn, encoding='UTF-8') as f:
    while s := f.read(1):
        alphabet = string.ascii_lowercase if s.islower() else string.ascii_uppercase
        pos = alphabet.find(s)
        if pos >= 0:
            ind = (pos + shift) % len(alphabet)
            ans.append(alphabet[ind])
        else:
            ans.append(s)

with open(fn_out, 'w') as f:
    f.write(''.join(ans))
