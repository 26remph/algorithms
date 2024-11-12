"""
Ловкость рук.
Игра «Тренажёр для скоростной печати»
"""

# id 68997972
from collections import Counter
from typing import List, Tuple


def get_sum(matrix: List[str], k: int) -> int:
    """Рассчитывает число баллов, которое смогут заработать участники."""
    cnt = Counter(matrix)
    return len(list(filter(lambda x: x <= k * 2, cnt.values())))


def read_input() -> Tuple[List[str], int]:
    """Считывает ввод данных"""
    k = int(input())
    matrix: list = []
    for _ in range(4):
        row = [x for x in input().strip() if x != "."]
        matrix = matrix + row
    return matrix, k


if __name__ == "__main__":
    arr, key = read_input()
    print(get_sum(arr, key))
