import re
import time

def get_pos(expr: str) -> int:

    pattern: str = r'\(|\)'

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

    stack: list = []
    matches = re.finditer(pattern, expr)
    pos: int = -1
    wrong_seq = []
    for match in matches:
        print(stack)
        if match[0] == '(':
            stack.append(match.end())
        if match[0] == ')':
            if not stack:
                # return -1
                wrong_seq.append(match.end())
                print(match, match.endpos, match.end())
                continue
            stack.pop()

    print('len(stack):', len(stack))
    print(stack)
    if len(stack) == 1:
        pos = stack.pop()

    if len(wrong_seq) == 1:
        print('--search--')

    print('wrong:', wrong_seq)


    return pos


def read_input() -> str:

    with open('input.txt', 'r') as f:
    # with open('inp_stapels_full.txt', 'r') as f:
        input_str: str = f.readline().strip()

    return input_str


if __name__ == '__main__':
    expression: str = read_input()
    start_time = time.time()
    with open('output.txt', 'w') as f:
        # print(get_pos(expression), file=f)
        print(get_pos(expression))

    print("--- %s seconds ---" % (time.time() - start_time))
