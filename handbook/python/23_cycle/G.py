a = int(input())
b = int(input())

a1, b1 = a, b

if a < b:
    a, b = b, a

while a > b > 1:
    a, b = b, a % b

gcd = b if b != 0 else a
lcm = a1 / gcd * b1

print(int(lcm))
