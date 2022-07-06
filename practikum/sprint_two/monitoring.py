from typing import Tuple, List, Dict


def read_input() -> Tuple[int, int]:
    n = int(input())
    m = int(input())
    return n, m


n, m = read_input()
t_matrix: Dict[int, List[str]] = {}
for _ in range(n):
    row: List[str] = list(map(str, input().split(' ')))
    for m, row_val in enumerate(row):
        if t_matrix.get(m):
            t_matrix[m].append(row_val)
        else:
            t_matrix[m] = [row_val]

del n, m

for _, val in t_matrix.items():
    print(' '.join(val))

