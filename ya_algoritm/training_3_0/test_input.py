# import fileinput
import sys
#
# cnt = 0
# with open('A_input.txt', encoding='utf8') as f:
#     while line := f.readline():
#         cnt += 1
#
# print(cnt)
#
# cnt = 0
# for line in fileinput.input('A_input.txt', encoding='utf8'):
#     cnt += 1
#
# print(cnt)

cnt = 0
for row in sys.stdin:
    cnt += 1

print(cnt)

