# ID 69340835
import operator

fabric = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack(list):
    pass


def read_input():
    return input().split(' ')


def calculator(row):

    stack = Stack()

    for ch in row:
        if ch in fabric.keys():

            x = int(stack.pop())
            y = int(stack.pop())
            func = fabric[ch]
            rez = func(y, x)
            stack.append(rez)
            continue

        stack.append(ch)

    return stack.pop()


if __name__ == '__main__':
    row = read_input()
    print(calculator(row))
