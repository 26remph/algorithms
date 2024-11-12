from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    x = int("".join(map(str, number_list)))
    rez_str = str(x + k)
    return [int(i) for i in rez_str]


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
