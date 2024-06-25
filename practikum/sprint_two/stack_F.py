class StackMax:

    def __init__(self):
        self.obj = []

    def is_empty(self):
        return not self.obj

    def get_max(self):
        print('None' if self.is_empty() else max(self.obj))

    def push(self, x):
        self.obj.append(x)

    def pop(self):
        if self.is_empty():
            print('error')
        else:
            self.obj.pop()


n = int(input())
stack = StackMax()

for _ in range(n):
    line: list = input().split(' ')
    command = line[0]
    params = None if len(line) < 2 else int(line[1])
    if params is not None:
        func = getattr(stack, command)
        func(params)
    else:
        func = getattr(stack, command)
        func()