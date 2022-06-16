"""
Ловкость рук.
Игра «Тренажёр для скоростной печати»
"""
# id 68972555
from typing import List, Tuple


def get_sum(matrix: List[str], k: int) -> int:
    """Рассчитывает число баллов, которое смогут заработать участники."""
    count: int = 0
    for char in set(matrix):
        if matrix.count(char) <= 2 * k:
            count += 1
    return count


def read_input() -> Tuple[List[str], int]:
    """Считывает ввод данных"""
    k = int(input())
    matrix: list = []
    for _ in range(4):
        row = [x for x in input().strip() if x != '.']
        matrix = matrix + row
    return matrix, k


arr, key = read_input()
print(get_sum(arr, key))
