class Rectangle:
    def __init__(self, dot1: tuple[float, float], dot2: tuple[float, float]):
        self.dot1 = dot1
        self.dot2 = dot2
        self.w = abs(self.dot2[0] - self.dot1[0])
        self.h = abs(self.dot2[1] - self.dot1[1])

    def area(self) -> float:
        return round(self.w * self.h, 2)

    def perimeter(self) -> float:
        return round(2 * (self.w + self.h), 2)

    def get_pos(self) -> tuple[float, float]:
        lx = min(self.dot1[0], self.dot2[0])
        ly = max(self.dot1[1], self.dot2[1])
        return round(lx, 2), round(ly, 2)

    def get_size(self) -> tuple[float, float]:
        return round(self.w, 2), round(self.h, 2)

    def move(self, dx: float, dy: float) -> None:
        self.dot1 = self.dot1[0] + dx, self.dot1[1] + dy
        self.dot2 = self.dot2[0] + dx, self.dot2[1] + dy

    def resize(self, width: float, height: float) -> None:
        self.w = width
        self.h = height
        lx, ly = self.get_pos()
        self.dot1 = lx + width, ly
        self.dot2 = lx, ly - height

    def get_center_pos(self):
        lx, ly = self.get_pos()
        return round(lx + self.w / 2, 2), round(ly - self.h / 2, 2)

    def turn(self):
        lc = self.get_center_pos()
        self.dot1 = lc[0] + self.h / 2, lc[1] + self.w / 2
        self.dot2 = self.dot1[0] - self.h, self.dot1[1] - self.w

        self.w, self.h = self.h, self.w

    def scale(self, factor: float) -> None:
        center = self.get_center_pos()
        self.w = self.w * factor
        self.h = self.h * factor
        self.dot1 = center[0] - self.w / 2, center[1] + self.h / 2
        self.dot2 = center[0] + self.w / 2, center[1] - self.h / 2


if __name__ == '__main__':
    print('--- example 1 ---')
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep='\n')
    rect.turn()
    print(rect.get_pos(), rect.get_size(), sep='\n')
    print('--- example 2 ---')
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep='\n')
    rect.scale(2.0)
    print(rect.get_pos(), rect.get_size(), sep='\n')
    print('--- example 3 ---')
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep='\n')
    rect.turn()
    rect.turn()
    rect.turn()
    # rect.turn()
    print(rect.get_pos(), rect.get_size(), sep='\n')