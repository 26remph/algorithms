# ID 69334279

class MyDequeueSized:

    def __init__(self, n):
        self.max_n = n
        self.queue = [None] * n
        self.tail = 0
        self.head = 0
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def push_back(self, x):
        if self.len != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.len += 1
        else:
            print('error')

    def push_front(self, x):
        if self.len != self.max_n:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_n
            self.len += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            print('error')
            return

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.len -= 1

        print(x)

    def pop_back(self):
        if self.is_empty():
            print('error')
            return


        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.len -= 1

        print(x)


if __name__ == '__main__':
    n = int(input())
    capacity = int(input())
    queue = MyDequeueSized(capacity)

    for _ in range(n):
        command, *params = input().split(' ')
        func = getattr(queue, command)
        func(*params)
