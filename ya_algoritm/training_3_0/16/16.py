import sys


class Queue:
    def __init__(self, k=1000):
        self.k = k
        self._seq = [None] * self.k
        self.head = -1
        self.tail = -1
        self._size = 1000

        self.debug = []

    def _extendseq(self):
        self.k = len(self._seq) + self._size
        head = self._seq[self.head :]
        tail = self._seq[: self.head]
        self._seq = head + tail + [None] * self._size
        self.head = 0
        self.tail = len(head + tail) - 1
        del head
        del tail

    def push(self, *args):
        n = args[0]

        self.tail += 1
        i = self.tail % self.k
        self.debug.append(f"{i}/{self.head}/{self.k}")

        if i != self.head:
            self._seq[i] = n
        else:
            self._extendseq()
            self.tail += 1
            self._seq[self.tail] = n

        self.head += 1 if self.head == -1 else 0

        # print(
        #     'ок', 'seq:', self._seq, 'h', self.head,
        #     't', self.tail, 'i', i, 'k', self.k
        # )
        print("ok")

    def pop(self):
        if self.head < 0:
            print("error")
        else:
            print(self._seq[self.head])
            self._seq[self.head] = None
            if self.head != self.tail:
                if self.head + 1 < self.k:
                    self.head += 1
                else:
                    self.head = 0
                    self.tail = self.tail % self.k
            else:
                self.head = -1
                self.tail = -1

    def front(self):
        if self.head < 0:
            print("error")
        else:
            print(self._seq[self.head])

    def size(self):
        print(self.tail - self.head + 1 if self.head != -1 else 0)

    def clear(self):
        self._seq = [0] * self.k
        self.head, self.tail = -1, -1
        print("ok")


q = Queue()
while (order := sys.stdin.readline().rstrip()) != "exit":
    name, *args = order.split(" ")
    func = getattr(q, name)
    func(*args)

print("bye")
