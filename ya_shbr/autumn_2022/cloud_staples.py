READ_SIZE_LIMIT = 2_000_000


def get_staples_pos():
    with open("input.txt", "r") as f:
        stack: list = []
        break_pos = -1

        pos: int = -1
        first_staples_pos = -1
        is_first = True
        shift: int = 0

        row: str = f.readline(READ_SIZE_LIMIT)
        while row:
            for ind, ch in enumerate(row):
                if ch == "{":
                    stack.append(ind + shift + 1)
                if ch == "}":
                    if is_first:
                        is_first = False
                        first_staples_pos = ind + shift + 1

                    if not stack:
                        if break_pos > 0:
                            break

                        break_pos = ind + shift + 1
                        continue

                    stack.pop()

            shift += READ_SIZE_LIMIT
            row = f.readline(READ_SIZE_LIMIT)

        if len(stack) == 1 and break_pos == -1:
            pos = stack.pop()

        if len(stack) == 0 and break_pos > 0:
            pos = first_staples_pos

        print(pos)


get_staples_pos()
