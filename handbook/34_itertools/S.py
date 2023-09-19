import itertools
import string

s = input()
var = list({x for x in s if x in string.ascii_uppercase})
var.sort()
print(*var, 'F')
for val in itertools.product(range(2), repeat=len(var)):
    d = {k: v for k, v in zip(var, val)}
    print(*val, 1 if eval(s, d) else 0)


