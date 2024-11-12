class Cell:
    def __init__(self, state: str):
        self.state = state

    def __repr__(self) -> str:
        return self.state

    def status(self) -> str:
        return self.state


class Checkers:
    cell = Cell
    rows_sign = "87654321"
    columns_sign = "ABCDEFGH"
    rows = 8
    column = 8

    def __init__(self):
        self.desk = [[self.cell("X") for _ in range(8)] for _ in range(8)]
        self.init_cell()

    def get_index_by_sign(self, col_sign: str, row_sign: str) -> tuple[int, int]:
        i = self.rows_sign.index(row_sign)
        j = self.columns_sign.index(col_sign)
        return i, j

    def init_cell(self):
        for i in range(self.rows):
            for j in range(self.column):
                if i % 2 != 0 and j % 2 == 0 or i % 2 == 0 and j % 2 != 0:
                    if i < 3:
                        self.desk[i][j] = self.cell("B")
                    elif i > 4:
                        self.desk[i][j] = self.cell("W")

    def move(self, f: str, t: str) -> None:
        st_i, st_j = self.get_index_by_sign(*list(f))
        end_i, end_j = self.get_index_by_sign(*list(t))
        cur_state = self.desk[st_i][st_j].status()
        if cur_state != "X":
            self.desk[st_i][st_j] = self.cell("X")
            self.desk[end_i][end_j] = self.cell(cur_state)

    def get_cell(self, p: str):
        i, j = self.get_index_by_sign(*list(p))
        return self.desk[i][j]

    def show_desk(self):
        for i in range(self.rows):
            print(self.desk[i])


if __name__ == "__main__":
    print("--example_1---")
    checkers = Checkers()
    checkers.show_desk()
    for row in "87654321":
        for col in "ABCDEFGH":
            # print(checkers.get_cell(col + row).status(), end='')
            print(checkers.get_cell(col + row), end="")
        print()

    print("--example_2---")
    checkers = Checkers()
    checkers.move("C3", "D4")
    checkers.move("H6", "G5")
    for row in "87654321":
        for col in "ABCDEFGH":
            print(checkers.get_cell(col + row).status(), end="")
        print()
