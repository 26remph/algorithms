class Rectangle(object):
    def __init__(self, dot1: tuple[float, float], dot2: tuple[float, float]):
        self.dot1 = dot1
        self.dot2 = dot2
        self.a = abs(self.dot2[0] - self.dot1[0])
        self.b = abs(self.dot2[1] - self.dot1[1])

    def area(self) -> float:
        return round(self.a * self.b, 2)

    def perimeter(self) -> float:
        return round(2 * (self.a + self.b), 2)


if __name__ == "__main__":
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.perimeter())
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.area())
