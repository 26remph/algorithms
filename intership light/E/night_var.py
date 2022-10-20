from collections import deque
from pprint import pprint


def calculate(dq, ingredient):

    dq.append('X')

    while dq:

        value = dq.popleft()
        if value == 'X':
            break

        # for value in _data:
        key = value[-2]
        # link = value[-1]

        sum_A, sum_B = 0, 0
        wrong = False
        for i in value[1:-2]:
            if i == 1:
                sum_A += 1
            elif i == 2:
                sum_B += 1
            else:
                content = ingredient.get(i, None)
                if content is None:
                    wrong = True
                    break

                sum_A += content[0]
                sum_B += content[1]

        if wrong:
            ingredient[key] = None
            dq.append(value)
        else:
            ingredient[key] = sum_A, sum_B

    dq.reverse()

    return dq, ingredient


with open('data.txt') as f:
    n = int(f.readline().rstrip())
# n = int(input())

    data = []
    key = 3
    # for _ in range(n - 2):
    while line := f.readline().rstrip():
        # row = list(map(int, input().split()))
        row = list(map(int, line.split()))
        row.append(key)
        row.append(max(row[1:-1]))

        data.append(row)
        key += 1

data.sort(key=lambda x: x[-1])
ing_amount = {key: None for key in range(3, n + 1)}

# print(data)

dq = deque(data)
# print('start dq:', len(dq), dq)
_len_before = len(dq)
_len_after = 0

while _len_before != _len_after:
    _len_before = len(dq)
    # print('\n_len_before', _len_before)
    dq, ing_amount = calculate(dq, ing_amount)
    _len_after = len(dq)
    # print('_len_after', _len_after)


# pprint(ing_amount)
# print('dq_after:', len(dq), dq)

q = int(input())
rez = []
for _ in range(q):
    row = list(map(int, input().split()))
    ing_A = row[0]
    ing_B = row[1]
    key = row[2]
    content = ing_amount.get(key)
    if content is None:
        rez.append('0')
        continue

    if content[0] <= ing_A and content[1] <= ing_B:
        rez.append('1')
    else:
        rez.append('0')

print(''.join(rez))
