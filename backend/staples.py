import re
from collections import Counter


def get_pos(expr: str) -> int:

    pattern: str = r'\(|\)'
    pattern_left: str = r'\('
    pattern_right: str = r'\)'
    pos: int = -1

    matches: list = re.findall(pattern, expr)
    open_left = True if matches[0] == '(' else False
    print(matches)
    print(open_left)

    cnt = Counter(matches)
    print(dict(cnt))
    print(cnt)
    print(len(cnt))

    if abs(cnt['('] - cnt[')']) == 1 and open_left:

    # if cnt['('] == cnt[')'] or abs(cnt['('] - cnt[')']) > 1 or len(cnt) == 0:
    #     return -1

        pattern = pattern_left if cnt['('] > cnt[')'] else pattern_right

        print(pattern)
        match = re.search(pattern, expr)
        if match:
            pos = match.end()
            print(match.start())
            print(match.end(), type(match))
        return pos

    return pos


def read_input() -> str:

    with open('input.txt', 'r') as f:
        input_str: str = f.readline().strip()

    return input_str


if __name__ == '__main__':
    expression: str = read_input()
    with open('output.txt', 'w') as f:
        print(get_pos(expression), file=f)

