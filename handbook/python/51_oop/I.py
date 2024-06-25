from typing import Any


class Node:
    next_node: object = None
    val: Any = None


class Queue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def push(self, item: Any) -> None:
        node = Node()
        node.val = item
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # print(self.head.val, self.tail.val, self.head == self.tail, self.tail is self.head)
            if self.head is self.tail:
                self.head.next_node = node
                self.tail = node
            else:
                self.tail.next_node = node
                self.tail = node

    def pop(self) -> Any:
        if self.head is not None:
            cur_node = self.head
            self.head = self.head.next_node

            val = cur_node.val
            cur_node.next_node = None
            del cur_node

            return val

    def is_empty(self) -> bool:
        return self.head is None


if __name__ == '__main__':
    print("--- example 1 ---")
    queue = Queue()
    for item in range(10):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop(), end=" ")

    print("--- example 2 ---")
    queue = Queue()
    for item in ("Hello,", "world!"):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop())