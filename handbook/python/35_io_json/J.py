from collections import deque
fn = input()
n = int(input())


deq = deque()
with open(fn, encoding="UTF-8") as f:
    for s in f:
        deq.append(s.rstrip())
        if len(deq) > n:
            deq.popleft()

for row in deq:
    print(row)
