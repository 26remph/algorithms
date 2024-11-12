import sys

from collections import Counter


class Stack:
    _seq = []
    cnt = Counter()

    def add(self, *args):
        n = args[0][0]
        key = args[0][1]
        for _ in range(n):
            self._seq.append(key)
        self.cnt.update({key: n})
        print("ok")

    def pop(self, *args):
        n = args[0][0]
        for _ in range(n):
            print(self._seq.pop() if self._seq else "error")

    def get(self):
        print(self._seq[-1] if self._seq else "error")


stack = Stack()
while (order := sys.stdin.readline().rstrip()) != "exit":
    name, *val = order.split(" ")
    func = getattr(stack, name)
    func(val)

print("bye")
