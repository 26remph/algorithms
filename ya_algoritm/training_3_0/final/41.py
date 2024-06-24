from collections import Counter


class Stack:

    _seq = []
    cnt = Counter()

    def add(self, *args):
        n = int(args[0][0])
        key = args[0][1]
        self._seq.append((key, n))
        self.cnt.update({key: n})

    def delete(self, *args):
        n = int(args[0][0])
        while self._seq and (val := self._seq.pop()):
            if val[1] <= n:
                self.cnt.subtract({val[0]: val[1]})
                n -= val[1]
            else:
                self._seq.append((val[0], val[1] - n))
                self.cnt.subtract({val[0]: n})
                break

    def get(self, *args):
        key = args[0][0]
        val = self.cnt.get(key)
        print(val if val is not None else 0)


N = int(input())
stack = Stack()
for _ in range(N):
    name, *val = input().split(' ')
    func = getattr(stack, name)
    func(val)
