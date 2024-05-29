rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
ans = ''.join([n * k for n, k in rle])
print(ans)