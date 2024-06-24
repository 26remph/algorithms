import random
import string

from b2 import prettywhile
from c2 import prettyfor


for _ in range(10_000):
    k = 10
    arr = []
    for _ in range(30):
        arr.append(random.choice(string.ascii_lowercase))
    s = ''.join(arr)
    assert prettyfor(k, s) == prettywhile(k, s), (k, s)

# k = 50
# s = 'pnwkexqnexjiljxkyhvgdxzpktcttnjwstwtowmupzullrzknjlgqyhutzftelcnzdogghzbhccrmvheoecjvpafekvllwijezhh'  # noqa: E501
# print(len(s))
# print('for:', prettyfor(k, s))
# print('while:', prettywhile(k, s))
# from  collections import Counter
# print(Counter(s).most_common())
# assert prettyfor(k, s) == prettywhile(k, s)
