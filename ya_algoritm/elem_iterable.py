# n = int(input())
# n_iter = [int(i) for i in input().split()]

# 'Variant 1'
print('-' * 25, 'Variant 1', '-' * 25)
with open('n_iter.txt', 'r') as f:
    n = int(f.readline())
    index = [int(i) for i in f.readline().split()]

# desired_iter = [
#     n_iter[ind-1] + n_iter[ind-3]
#     for ind, i in enumerate(n_iter) if ind > 3
# ]
# f(x) = f(x-1) + f(x-3)

max_index = max(index)

in_mem = (0, 1, 2, 2)


def foo(ind):
    global in_mem
    # print('ind=', ind)
    # print("in_mem", in_mem)
    if ind <= 3:
        return in_mem[ind]

    val = in_mem[-1] + in_mem[-3]
    # print("val", val)
    in_mem = (in_mem[-3], in_mem[-2], in_mem[- 1], val)
    # print("in_mem", in_mem)
    return val


desired_iter = [foo(ind) for ind in range(max_index + 1)]

print('idex=', index)
# print('desired_iter=', ' '.join(str(e) for ind, e in enumerate(desired_iter) if ind in index))

for ind in index:
    print(desired_iter[ind], end=' ')

# 'Variant 2 official solution'
print('\n', '-' * 25, 'Variant 2', '-' * 25)

with open('n_iter.txt', 'r') as f:
    n = int(f.readline())
    indices = [int(i) for i in f.readline().split()]

print('indices=', indices)
results = {i: i if i < 3 else None for i in indices}
print(type(results))
print('results=', results)
k = max(indices)
print('k=', k)
a, b, c = 0, 1, 2
for i in range(3, k + 1):
    a, b, c = b, c, a + c
    if i in results:
        results[i] = c
print(" ".join(str(results[i]) for i in indices))

# class DesiredIter(list):
#     pass
