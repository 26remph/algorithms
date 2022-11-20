from collections import Counter
from array import array
n = int(input())
# По условию задачи X и Y не больше 10^9
max_x_y = 2 ** 30

# Индекс, количество А, количество B, количество не расш. инргид., список зелий в которых участвует ингридиент
p = array('L', (0 for _ in range(n << 2)))
p[0], p[4 + 1] = 1, 1
pp = [[] for _ in range(n)]
for index in range(2, n):
    k = Counter(list(map(int, input().split()[1:])))
    for key, count in k.items():
        pp[key - 1].append((index, count))
    p[(index << 2) + 2] = len(k)
stack = [0, 1]
stack_index = 0
while stack_index < len(stack):
    index = stack[stack_index]
    index_4 = index << 2
    for key, count in pp[index]:
        base = key << 2
        p[base + 2] -= 1
        if p[base] < max_x_y:
            p[base] += min(p[index_4] * count, max_x_y)
        if p[base + 1] < max_x_y:
            p[base + 1] += min(p[index_4 + 1] * count, max_x_y)
        if p[base + 2] <= 0:
            stack.append(key)
    stack_index += 1
q = int(input())
result = []
for _ in range(q):
    x, y, s = map(int, input().split())
    base = (s - 1) << 2
    result.append("1" if p[base + 2] <= 0 and p[base] <= x and p[base + 1] <= y else "0")
print("".join(result))