from collections import defaultdict


n = int(input())
surname = defaultdict(int)
for _ in range(n):
    surname[input()] += 1

print(sum([c for f, c in surname.items() if c > 1]))