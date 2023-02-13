from collections import defaultdict
from collections import deque
N = int(input())

tree = defaultdict(list)
topic = {}
for i in range(1, N+1):
    num = int(input())

    if num == 0:
        tree[num].append(i)
        topic[i] = input()
        _ = input()
    else:
        tree[num].append(i)
        _ = input()

topics = []
max_cnt = 0
for root in topic.keys():
    visited = deque(tree[root])
    cnt = 0
    while visited:
        node = tree[visited.popleft()]
        visited.extend(node)
        cnt += 1

    topics.append((topic[root], cnt))

print(max(topics, key=lambda x: x[1])[0])


