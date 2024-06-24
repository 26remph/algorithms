# a != b (исключающее или)
# not a or b (импликация) # a <= b
# a == b (эквиваленция)
import itertools


x, y = False, False
print(x <= y)
print(not x or y)

for x, y in itertools.product(range(2), repeat=2):
    assert (x <= y) == (not x or y)
    print(x, y, '-> equal')