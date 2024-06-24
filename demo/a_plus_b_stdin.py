from typing import Tuple


def get_sum(a: int, b: int) -> int:
    return a + b


def read_input() -> Tuple[int, int]:
    values: list = list(map(int, input().strip().split()))
    a = values[0]
    b = values[1]
    return a, b


a, b = read_input()
print(get_sum(a, b))
