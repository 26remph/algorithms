numbers = [15, 49, 36]
d = {key: [x for x in range(1, key + 1) if not key % x] for key in numbers}
print(d)