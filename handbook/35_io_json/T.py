fn = 'numbers.num'
with open(fn, 'rb') as f:
    summa = 0
    while byte := f.read(2):
        summa += int(bytes.hex(byte), 16)

print(summa % 65_536)