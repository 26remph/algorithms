import sys

# int_num = 1000
#
# print('int=', sys.getsizeof(int_num))
#
# array_a = (1000 for i in range(1000))
#
# print('array_=a', sys.getsizeof(array_a))
#
# array_b: list = []
# print('array_=b', sys.getsizeof(array_b))
# print(array_b)
#
# for i in array_a:
#     array_b.append(i+1)
#     array_b.append(i+3)
#
#
# print('array_=b', sys.getsizeof(array_b), 'b')
# print(array_b)

# 'Variant 1'
print('\n', '-' * 25, 'Variant 1', '-' * 25)
ai, bi, aj, bj = [], [], [], []

with open('input_join.txt', 'r') as f:
    n1 = int(f.readline())
    for elem in range(n1):
        vect = list(map(int, f.readline().split()))
        ai.append(vect[0])
        bi.append(vect[1])
    n2 = int(f.readline())
    for elem in range(n2):
        vect = list(map(int, f.readline().split()))
        aj.append(vect[0])
        bj.append(vect[1])
    join = f.readline()

print(n1, n2, ai, bi, aj, bj, join)

