class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def set_next(self, next_node):
        self.next = next_node


class MyQueueLinkedList:
    def __init__(self):
        # self.queue = []
        self.tail = None
        self.head = None
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def put(self, x):
        if self.head is None:
            node = Node(x)

            self.head = node
            self.tail = node
            self.len += 1
            return

        node = Node(x)
        self.tail.set_next(node)

        self.tail = node
        self.len += 1

    def get(self):
        if self.is_empty():
            print("error")
            return

        x = self.head
        self.head = self.head.next
        self.len -= 1
        print(x.value)
        del x

    def size(self):
        print(self.len)


n = int(input())
queue = MyQueueLinkedList()

for _ in range(n):
    command, *params = input().split(" ")
    func = getattr(queue, command)
    func(*params)
