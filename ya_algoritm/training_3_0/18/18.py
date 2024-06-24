import sys

from collections import deque


class Deque:
    _seq = deque()

    def push_front(self, n):
        self._seq.appendleft(n)
        print('ok')

    def push_back(self, n):
        self._seq.append(n)
        print('ok')

    def pop_front(self, *args, **kwargs):
        print('error' if not self._seq else self._seq.popleft())

    def pop_back(self, *args, **kwargs):
        print('error' if not self._seq else self._seq.pop())

    def front(self, *args, **kwargs):
        print('error' if not self._seq else self._seq[0])

    def back(self, *args, **kwargs):
        print('error' if not self._seq else self._seq[-1])

    def size(self, *args, **kwargs):
        print(len(self._seq))

    def clear(self, *args, **kwargs):
        self._seq.clear()
        print('ok')


deq = Deque()
while (order := sys.stdin.readline().rstrip()) != 'exit':
    name, *param = order.split(' ')
    func = getattr(deq, name)
    func(*param)

print('bye')