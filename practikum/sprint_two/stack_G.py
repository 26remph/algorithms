class StackMaxEffective:

    def __init__(self):
        self.obj = []
        self.max = []

    def is_empty(self):
        return False if self.obj else True

    def peek_max(self):

        assert len(self.obj) == len(self.max)

        if self.max:
            # print('--- peek ---')
            # print('obj', self.obj)
            # print('max', self.max)
            # print('peek', self.max[-1])
            return self.max[-1]
        else:
            return None

    def get_max(self):
        print('None' if self.is_empty() else self.peek_max())
        assert len(self.obj) == len(self.max)
        if self.obj:
            assert self.peek_max() == max(self.obj)
        else:
            assert  self.peek_max() is None

    def push(self, x):
        last_max = self.peek_max()

        if last_max is not None:
            self.max.append(max(x, last_max))
        else:
            self.max.append(x)

        self.obj.append(x)

        # print('--- push ---')
        # print('last_max:', last_max)
        # print('obj', self.obj)
        # print('max', self.max)
        # print('peek', self.max[-1])

        assert len(self.obj) == len(self.max)


    def pop(self):
        if self.is_empty():
            print('error')
        else:
            self.obj.pop()
            self.max.pop()

        assert len(self.obj) == len(self.max)


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