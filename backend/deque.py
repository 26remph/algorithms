from collections import deque

q = deque()
if not q:
    print('--empty--')
q.append('a')
q.append('b')
q.append('c')
print('len q:', len(q))
print('Initial queue')
print(q)
print('\nElements dequeued from the queue')
print(q.popleft())
print(q.popleft())
print(q.popleft())
print('\nQueue after removing elements')
print(q)
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
