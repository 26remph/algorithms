from sys import stdin


summa = 0
for row in stdin:
    summa += sum(map(int, row.split()))

print(summa)
