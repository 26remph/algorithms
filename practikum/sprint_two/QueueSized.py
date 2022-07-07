class MyQueueSized:

    def __init__(self, n):
        self.max_n = n
        self.queue = [None] * n
        self.tail = 0
        self.head = 0
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def push(self, x):
        if self.len != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.len += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            print('None')
            return

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.len -= 1

        print(x)

    def peek(self):
        if self.is_empty():
            print('None')
            return

        print(self.queue[self.head])

    def size(self):
        print(self.len)


n = int(input())
capacity = int(input())
queue = MyQueueSized(capacity)

for _ in range(n):
    command, *params = input().split(' ')
    func = getattr(queue, command)
    func(*params)
