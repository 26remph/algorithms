from itertools import count


start, end, step = map(float, input().split())
for num in count(start, step):
    if num >= end:
        break
    print(f"{num:.2f}")
