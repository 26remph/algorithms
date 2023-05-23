def get_pos(expr: str) -> int:

    stack: list = []
    wrong_seq: list = []

    pos: int = -1
    min_pos = -100
    first_pos = True

    for ind, symbol in enumerate(expr):
        if symbol == '{':
            stack.append(ind + 1)
        if symbol == '}':
            if first_pos:
                first_pos = False
                min_pos = ind + 1

            if not stack:
                if len(wrong_seq) > 1:
                    break
                wrong_seq.append(ind + 1)
                continue

            stack.pop()

    if len(stack) == 1 and len(wrong_seq) == 0:
        pos = stack.pop()

    if len(wrong_seq) == 1 and len(stack) == 0:
        return min_pos

    return pos


def read_input() -> list:

    with open('./input.txt', 'r') as f:
        input_str: list = f.readlines()

    return input_str

str_datas: list = read_input()
# print(get_pos(str_data))
with open('output.txt', 'w') as f:
    for row in str_datas:
        print(get_pos(row), file=f)

