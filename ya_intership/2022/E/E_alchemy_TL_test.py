import time


start = time.time()
with open('data.txt') as f:
    n = int(f.readline().rstrip())
    # n = int(input())
    while line := f.readline().rstrip():
        data = []
        key = 3
        for _ in range(n - 2):
            row = list(map(int, line.split()))
            row.append(key)
            row.append(max(row[1:-1]))

            data.append(row)
            key += 1

        data.sort(key=lambda x: x[-1])

        ing_amount = {key: None for key in range(3, n + 1)}
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

print(f'read time: {time.time() - start} seconds')
# print(ing_amount)

start_query = time.time()
with open('query.txt') as f:
    q = int(f.readline().rstrip())
    # q = int(input())
    rez = []
    while line := f.readline().rstrip():
        # print(line)
        # for _ in range(q):
        row = list(map(int, line.split()))
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


# print(''.join(rez))
print(f'query time: {time.time() - start_query}')
print(f'total time: {time.time() - start} seconds')
