import math


x, y = map(float, input().split())
p, fi = map(float, input().split())

x1, y1 = p * math.cos(fi), p * math.sin(fi)

dist = pow(pow(x1 - x, 2) + pow(y1 - y, 2), 0.5)
print(dist)
