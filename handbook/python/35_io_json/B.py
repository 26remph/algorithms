from sys import stdin

before = 0
after = 0
cnt = 0
for row in stdin:
    _, b, a = row.split()
    cnt += 1
    before += int(b)
    after += int(a)

print(round((after - before) / cnt))
