# ID 69334279
from typing import List

SIGN = ('+', '-', '*', '/')


def read_input():
    return input().split(' ')


def calculator(row):

    stack: List[str] = []

    for ch in row:
        if ch in SIGN:

            x = str(stack.pop())
            y = str(stack.pop())
            if ch == '/':
                ch = '//'
            expression = f'{y} {ch} {x}'
            code = compile(expression, '<string>', mode='eval')
            rez = eval(code, {"__builtins__": {}}, {'x': x, 'y': y})
            stack.append(rez)
            continue

        stack.append(ch)

    return stack.pop()


if __name__ == '__main__':
    row = read_input()
    print(calculator(row))