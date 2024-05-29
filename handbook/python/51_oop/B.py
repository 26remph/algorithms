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


if __name__ == '__main__':
    # first example
    point = Point(3, 5)
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)
    # second example
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))