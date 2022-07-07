from typing import Tuple


def get_sum(a: int, b: int) -> int:
    return a + b


def read_input() -> Tuple[int, int]:

    with open('input.txt', 'r') as f:
        values: list = list(map(int, f.readline().strip().split()))

    a = values[0]
    b = values[1]
    return a, b


a, b = read_input()
with open('output.txt', 'w') as f:
    print(get_sum(a, b), file=f)

