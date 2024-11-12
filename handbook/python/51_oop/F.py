import random


class Rectangle:
    def __init__(self, dot1: tuple[float, float], dot2: tuple[float, float]):
        self.dot1 = dot1
        self.dot2 = dot2
        self.a = abs(self.dot2[0] - self.dot1[0])
        self.b = abs(self.dot2[1] - self.dot1[1])

    def area(self) -> float:
        return round(self.a * self.b, 2)

    def perimeter(self) -> float:
        return round(2 * (self.a + self.b), 2)

    def get_pos(self) -> tuple[float, float]:
        lx = min(self.dot1[0], self.dot2[0])
        ly = max(self.dot1[1], self.dot2[1])
        return round(lx, 2), round(ly, 2)

    def get_size(self) -> tuple[float, float]:
        return round(self.a, 2), round(self.b, 2)

    def move(self, dx: float, dy: float) -> None:
        self.dot1 = self.dot1[0] + dx, self.dot1[1] + dy
        self.dot2 = self.dot2[0] + dx, self.dot2[1] + dy

    def resize(self, width: float, height: float) -> None:
        self.a = width
        self.b = height
        lx, ly = self.get_pos()
        self.dot1 = lx + width, ly
        self.dot2 = lx, ly - height


if __name__ == "__main__":
    print("--- first example")
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.move(1.32, -5)
    print(rect.get_pos(), rect.get_size())
    print("--- second example ---")
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())

    for _ in range(10000):
        x = random.random()
        y = random.random()
        r = Rectangle((x, y), (x * random.randint(-2, 2), y * random.randint(-2, 2)))
        Rectangle((0, 0), (0, 0))
