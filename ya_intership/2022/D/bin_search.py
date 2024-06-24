from bisect import bisect_left, bisect_right


# data = [('red', 5), ('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data = [
    ('red', 5), ('red', 5), ('red', 5), ('red', 5), ('blue', 1),
    ('yellow', 4), ('black', 0), ('green', 10), ('borrow', 12)
]
# Или `key=operator.itemgetter(1)`
data.sort(key=lambda r: r[1])
print(data, len(data))
# Предварительно вычислим список ключей.
keys = [r[1] for r in data]
ind = bisect_left(keys, 6)
x = data[bisect_left(keys, 6)]
print(x, ind)
ind = bisect_right(keys, 5)
x = data[bisect_right(keys, 5)]
print(x, ind)

# ('black', 0)
# x = data[bisect_left(keys, 1)]
# print(x)
# # ('blue', 1)
# x = data[bisect_left(keys, 5)]
# print(x)
# # ('red', 5)
# x = data[bisect_left(keys, 8)]
# print(x)
# # ('yellow', 8)
