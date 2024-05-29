from collections import defaultdict

words = defaultdict(int)
while s := input():
    for key in s.split():
        words[key] += 1

for key, val in words.items():
    print(key, val)
