import re
from collections import Counter


def get_pos(expr: str) -> int:

    pattern: str = r'\(|\)'
    pattern_left: str = r'\('
    pattern_right: str = r'\)'
    pos: int = -1

    matches: list = re.findall(pattern, expr)
    open_left = False
    if matches:
        open_left = True if matches[0] == '(' else False

    cnt = Counter(matches)

    if abs(cnt['('] - cnt[')']) == 1 and open_left:

        pattern = pattern_left if cnt['('] > cnt[')'] else pattern_right
        match = re.search(pattern, expr)
        if match:
            pos = match.end()

        return pos

    return pos


def read_input() -> str:

    with open('input.txt', 'r') as f:
        input_str: str = f.readline().strip()

    return input_str


if __name__ == '__main__':
    expression: str = read_input()
    # start_time = time.time()
    with open('output.txt', 'w') as f:
        print(get_pos(expression), file=f)
    # print("--- %s seconds ---" % (time.time() - start_time))