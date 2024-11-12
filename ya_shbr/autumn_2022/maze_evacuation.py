import random

from typing import List, Optional, Tuple


def get_directions(
    point: Optional[Tuple[int, int, str]], maze
) -> List[Optional[Tuple[int, int, str]]]:
    if point is None:
        return [None, None, None, None]

    x, y = point[0], point[1]
    left = (x, y + 1, "L") if maze[x][y + 1] == "." else None
    right = (x, y - 1, "R") if maze[x][y - 1] == "." else None
    up = (x + 1, y, "U") if maze[x + 1][y] == "." else None
    down = (x - 1, y, "D") if maze[x - 1][y] == "." else None

    directions = [right, down, left, up]

    return directions


def get_step(directions) -> Tuple[Optional[Tuple[int, int, str]], bool]:
    f_dir = [x for x in directions if x is not None]
    is_fork = len(f_dir) > 1

    if len(f_dir) == 0:
        return None, is_fork

    cur_point: Optional[Tuple[int, int, str]] = random.choices(f_dir)[0]

    return cur_point, is_fork


def mark_point(cur_point: Optional[Tuple[int, int, str]], maze) -> None:
    if cur_point is not None:
        x, y, ch = cur_point
        maze[x][y] = ch


def put_fork(point, directions):
    on_steak = [x for x in directions if x is not None and x != point]
    return on_steak


def foo(maze: List[List[str]], enter_point: Tuple[int, int, str]) -> List[List[str]]:
    cur_point: Optional[Tuple[int, int, str]] = enter_point
    forks = [enter_point]

    while len(forks) != 0:
        mark_point(cur_point, maze)
        directions = get_directions(cur_point, maze)

        cur_point, is_fork = get_step(directions)

        if cur_point is not None:
            if is_fork:
                forks = forks + put_fork(cur_point, directions)
        else:
            cur_point = forks.pop()

    return maze


def read_input() -> Tuple[List[List[str]], Tuple[int, int, str]]:
    n, _ = map(int, input().strip().split())
    maze: List[List[str]] = []
    s_point: Tuple[int, int, str] = (-1, -1, "")
    for i in range(n):
        row: list = []
        for ind, j in enumerate(input()):
            row.append(j)
            if j == "S":
                s_point = (i, ind, "S")
        maze.append(row)

    return maze, s_point


def print_result(result: List[List[str]]) -> None:
    for row in result:
        print("".join(row))


matrix, enter = read_input()
print_result(foo(matrix, enter))
