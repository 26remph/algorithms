import math


x = float(input())
fx = (
    math.log(math.pow(x, 3 / 16), 32)
    + math.pow(x, math.cos(math.pi * x / (2 * math.e)))
    - math.pow(math.sin(x / math.pi), 2)
)

print(fx)
