import math

from typing import TypeVar


Dot = TypeVar("Dot", bound="Point")


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
    def __init__(
        self, val1: int | tuple[int, int] = 0, val2: int | tuple[int, int] = 0
    ) -> None:
        if isinstance(val1, tuple):
            super().__init__(*val1)
        else:
            super().__init__(val1, val2)

    def __add__(self, other: tuple) -> Dot:
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other: tuple) -> Dot:
        self.x += other[0]
        self.y += other[1]
        return self

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__class__.__name__ + f"({self.x}, {self.y})"


if __name__ == "__main__":
    point = PatchedPoint()
    print(point)
    new_point = point + (2, -3)
    print(point, new_point, point is new_point)

    first_point = second_point = PatchedPoint((2, -7))
    first_point += (7, 3)
    print(first_point, second_point, first_point is second_point)
