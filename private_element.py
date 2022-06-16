
# Variant - 1
print('-' * 25, 'Variant 1', '-' * 25)
with open('input_data.txt', 'r') as f:
    n = f.readline()
    array = list(map(int, f.readline().split()))


print(array, type(array))
sort_array = sorted(array, key=lambda x: array.count(x), reverse=True)
print('sort_array=', sort_array)
print(sort_array[0])
print(f'frequency={sort_array.count(sort_array[0])}')

# Variant - 2
print('-' * 25, 'Variant 2', '-' * 25)
from collections import Counter

with open('input_data.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]

counter = Counter(a)
result = a[0]
max_count = counter[result]
print('result=', result)
print('max_count=', max_count)
print('counter elements=', counter.elements())
for el in counter.elements():
    print('el=', el)
print(sorted(counter.elements()))
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result)

# 'Variant 3'
print('-' * 25, 'Variant 3', '-' * 25)
with open('input_data.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]

counter = Counter(a)
print("most common method=", counter.most_common())
print(counter.most_common(1), type(counter.most_common(1)))
print(counter.most_common(1)[0][0])
print(+counter)










