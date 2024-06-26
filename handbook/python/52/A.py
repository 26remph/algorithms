import math

from typing import TypeVar


Dot = TypeVar('Dot', bound='Point')


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, p: Dot) -> float:
        l1 = pow(abs(self.x - p.x), 2) + pow(abs(self.y - p.y), 2)
        return round(math.sqrt(l1), ndigits=2)


class PatchedPoint(Point):
    def __init__(self, val1: int | tuple[int, int] = 0, val2: int | tuple[int, int] = 0
                 ) -> None:
        if isinstance(val1, tuple):
            super().__init__(*val1)
        else:
            super().__init__(val1, val2)


if __name__ == '__main__':
    point = PatchedPoint()
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)

    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))