# Алгоритм Евклида
# https://ru.wikipedia.org/wiki/Алгоритм_Евклида

a = int(input())
b = int(input())

if a < b:
    a, b = b, a

while a > b > 1:
    a, b = b, a % b

print(b if b != 0 else a)
