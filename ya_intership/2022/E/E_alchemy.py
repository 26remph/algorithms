from pprint import pprint


n = int(input())
data = []
key = 3
for _ in range(n - 2):
    row = list(map(int, input().split()))
    row.append(key)
    row.append(max(row[1:-1]))

    data.append(row)
    key += 1

data.sort(key=lambda x: x[-1])
ing_amount = dict.fromkeys(range(3, n + 1))
print(data)

for value in data:
    key = value[-2]
    link = value[-1]

    sum_A, sum_B = 0, 0
    wrong = False
    for i in value[1:-2]:
        if i == 1:
            sum_A += 1
        elif i == 2:
            sum_B += 1
        else:
            content = ing_amount.get(i)
            if content is None:
                wrong = True
                break

            sum_A += content[0]
            sum_B += content[1]

    if wrong:
        ing_amount[key] = None
    else:
        ing_amount[key] = sum_A, sum_B

pprint(ing_amount)

q = int(input())
rez = []
for _ in range(q):
    row = list(map(int, input().split()))
    ing_A = row[0]
    ing_B = row[1]
    key = row[2]
    content = ing_amount.get(key)
    if content is None:
        rez.append("0")
        continue

    if content[0] <= ing_A and content[1] <= ing_B:
        rez.append("1")
    else:
        rez.append("0")

print("".join(rez))
