class StackMaxEffective:

    def __init__(self):
        self.obj = []
        self.max = []

    def is_empty(self):
        return False if self.obj else True

    def peek_max(self):
        if self.max:
            return self.max[-1]
        else:
            return None

    def get_max(self):
        # print('--- get_max ---')
        # print('obj:', self.obj)
        # print('max:', self.max)
        print('None' if self.is_empty() else self.peek_max())

    def push(self, x):
        last_max = self.peek_max()
        self.obj.append(x)
        if last_max:
            self.max.append(max(x, last_max))
        else:
            self.max.append(x)

        # print('--- push ---')
        # print('obj:', self.obj)
        # print('max:', self.max)

    def pop(self):
        if self.is_empty():
            print('error')
        else:
            self.obj.pop()
            self.max.pop()


n = int(input())
stack = StackMaxEffective()

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