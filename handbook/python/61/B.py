import math
import sys

for row in sys.stdin:
    arr = map(int, row.split())
    print(math.gcd(*arr))