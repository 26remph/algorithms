import sys
from collections import deque
voices = {}

cnt_num = 0
# for line in sys.stdin:
while line := sys.stdin.readline().rstrip():
    values = line.split()
    num = int(values.pop())
    key = ' '.join(values)
    voices[key] = num
    cnt_num += num

K1 = cnt_num / 450
# print('total_voice', cnt_num)
# print('K1', K1)
# print(voices)

total_place = 0

rez = []
for key, value in voices.items():

    int_part = value // K1 if K1 else K1
    rem_part = value % K1 if K1 else K1

    # print('int_part', int_part)
    # print('rem_part', rem_part)

    voices[key] = int_part
    rez.append((rem_part, voices[key], key))
    total_place += int_part

# print('total_place', total_place)
rez.sort(key=lambda x: (-x[0], x[1]))
# print('rez', rez)

deq = deque(rez)
if total_place < 450:
    remains = 450 - total_place
    while remains != 0:
        val = deq.popleft()
        voices[val[2]] += 1
        remains -= 1
        deq.append(val)

for key, val in voices.items():
    print(key, int(val))



