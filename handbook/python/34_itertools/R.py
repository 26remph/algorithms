import itertools


s = input()
print('a', 'b', 'c', 'f')
for a, b, c in itertools.product([0, 1], repeat=3):
    print(a, b, c, 1 if eval(s) else 0)
