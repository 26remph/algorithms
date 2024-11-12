class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    print("--- example 1 ---")
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end=" ")

    print("--- example 2 ---")
    stack = Stack()
    for item in ("Hello,", "world!"):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())
