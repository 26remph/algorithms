from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int,
                   col: int, n: int, m: int) -> List[int]:

    left = matrix[row][col - 1] if col - 1 >= 0 else None
    right = matrix[row][col + 1] if col + 1 < m else None
    upper = matrix[row - 1][col] if row - 1 >= 0 else None
    down = matrix[row + 1][col] if row + 1 < n else None
    rez = [x for x in (left, right, upper, down) if x is not None]
    return sorted(rez)


def read_input() -> Tuple[List[List[int]], int, int, int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m


matrix, row, col, n, m = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col, n, m))))