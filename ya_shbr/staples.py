import re

from collections import deque


def get_pos(expr: str) -> int:
    pattern: str = r"\(|\)"

    matches = re.finditer(pattern, expr)
    count = 0
    pos: int = -1
    for match in matches:
        count += 1
        if count > 1:
            break
        pos = match.end()

    if count == 0:
        return -1
    elif count == 1:
        return pos

    # stack: list = []
    stack = deque()
    matches = re.finditer(pattern, expr)
    pos: int = -1
    wrong_seq: list = []
    for match in matches:
        if match[0] == "(":
            stack.append(match.end())
        if match[0] == ")":
            if not stack:
                # return -1
                if len(wrong_seq) > 1:
                    break
                wrong_seq.append(match.end())
                continue

            stack.pop()

    if len(stack) == 1 and len(wrong_seq) == 0:
        pos = stack.pop()

    if len(wrong_seq) == 1 and len(stack) == 0:
        match = re.search(r"\)", expr)
        if match:
            pos = match.end()
            return pos

    return pos


def read_input() -> str:
    with open("input.txt", "r") as f:
        input_str: str = f.readline().strip()

    return input_str


expression: str = read_input()
with open("output.txt", "w") as f:
    print(get_pos(expression), file=f)
