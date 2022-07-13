# ID 69343342
import operator

FABRIC = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack():
    def __init__(self):
        self.__items = []

    def pop(self):
        return self.__items.pop()

    def push(self, item):
        return self.__items.append(item)

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


def read_input():
    return input().split(' ')


def calculator(row):

    stack = Stack()

    for ch in row:
        if ch in FABRIC.keys():

            x = int(stack.pop())
            y = int(stack.pop())
            func = FABRIC[ch]
            rez = func(y, x)
            stack.push(rez)
            continue

        stack.push(ch)

    return stack.pop()


if __name__ == '__main__':
    row = read_input()
    print(calculator(row))
