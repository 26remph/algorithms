import random

from check import RectangleCheck


class Rectangle:
    def __init__(self, dot1: tuple[float, float], dot2: tuple[float, float]):
        self.left_corner = (min(dot1[0], dot2[0]), max(dot1[1], dot2[1]))
        self.w = round(abs(dot2[0] - dot1[0]), 2)
        self.h = round(abs(dot2[1] - dot1[1]), 2)

    def area(self) -> float:
        return round(self.w * self.h, 2)

    def perimeter(self) -> float:
        return round(2 * (self.w + self.h), 2)

    def get_pos(self) -> tuple[float, float]:
        return round(self.left_corner[0], 2), round(self.left_corner[1], 2)

    def get_size(self) -> tuple[float, float]:
        return round(self.w, 2), round(self.h, 2)

    def move(self, dx: float, dy: float) -> None:
        lx = round(self.left_corner[0] + dx, 2)
        ly = round(self.left_corner[1] + dy, 2)
        self.left_corner = lx, ly

    def resize(self, width: float, height: float) -> None:
        self.w = round(width, 2)
        self.h = round(height, 2)

    def turn(self):
        dx = dy = round((self.w - self.h) / 2, 2)
        self.move(dx, dy)
        self.w, self.h = self.h, self.w

    def scale(self, factor: float) -> None:
        dx = round((self.w * (factor - 1)), 2)
        dy = round((self.h * (factor - 1)), 2)
        self.move(-dx / 2, dy / 2)
        self.resize(self.w * factor, self.h * factor)


if __name__ == "__main__":
    print("--- example 1 ---")
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep="\n")
    rect.turn()
    print(rect.get_pos(), rect.get_size(), sep="\n")
    print("--- example 2 ---")
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep="\n")
    rect.scale(2.0)
    print(rect.get_pos(), rect.get_size(), sep="\n")
    print("--- example 3 ---")
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep="\n")
    rect.turn()
    rect.turn()
    print(rect.get_pos(), rect.get_size(), sep="\n")

    # test class
    # method = ['turn', 'scale', 'get_pos']
    method = ["scale", "get_pos"]
    for _ in range(1):
        dot1 = (random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0))
        dot2 = (random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0))
        rect = Rectangle(dot1, dot2)
        rect_check = RectangleCheck(dot1, dot2)
        print("> rect", dot1, dot2, "tested")
        for _ in range(10):
            func_name = random.choice(method)
            param = None
            if func_name == "scale":
                param = random.uniform(0.0, 10.0)
                val = getattr(rect, func_name)(param)
                val_check = getattr(rect_check, func_name)(param)
            else:
                val = getattr(rect, func_name)()
                val_check = getattr(rect_check, func_name)()

            assert val == val_check, f"{func_name=}({val=}, {val_check=})"
            print(func_name, param, val, val_check, "ok")
