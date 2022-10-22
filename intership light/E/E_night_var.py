from collections import deque


def calculate(deq, ingredient):

    deq.append('X')
    while deq:
        value = deq.popleft()
        if value == 'X':
            break

        _id = value[-2]

        col_a, col_b = 0, 0
        err = False
        for i in value[1:-2]:
            if i == 1:
                col_a += 1
            elif i == 2:
                col_b += 1
            else:
                x = ingredient.get(i, None)
                if x is None:
                    err = True
                    break

                col_a += x[0]
                col_b += x[1]

        if err:
            ingredient[_id] = None
            deq.append(value)
        else:
            ingredient[_id] = col_a, col_b

    deq.reverse()
    return deq, ingredient


n = int(input())

# arr = []
dq = deque()
key = 3
for _ in range(n - 2):
    row = list(map(int, input().split()))
    row.append(key)
    max_ing = max(row[1:-1])
    row.append(max_ing)
    if max_ing > 2:
        dq.appendleft(row)
    else:
        dq.append(row)
    key += 1

# arr.sort(key=lambda x: x[-1])
ing_amount = {key: None for key in range(3, n + 1)}

# dq = deque(arr)
_len_before = len(dq)
_len_after = 0

while _len_before != _len_after:
    _len_before = len(dq)
    dq, ing_amount = calculate(dq, ing_amount)
    _len_after = len(dq)

q = int(input())
out = []
for _ in range(q):
    row = list(map(int, input().split()))
    inc_a, inc_b, key = row[0], row[1], row[2]

    x = ing_amount.get(key)
    if x is None:
        out.append('0')
        continue

    out.append('1') if x[0] <= inc_a and x[1] <= inc_b else out.append('0')

print(''.join(out))
