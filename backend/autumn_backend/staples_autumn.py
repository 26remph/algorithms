
# memory_limit = 16_000_000

memory_limit = 160

def get_min_pos():

    with open('./input.txt', 'r') as f:

        stack: list = []
        wrong_seq: list = []

        pos: int = -1
        min_pos = -100
        first_pos = True
        shift: int = 0

        input_str: str = f.readline(memory_limit)
        while input_str:
            # print(input_str, len(input_str))
            for ind, symbol in enumerate(input_str):
                if symbol == '{':
                    stack.append(ind + 1 + shift)
                if symbol == '}':
                    if first_pos:
                        first_pos = False
                        min_pos = ind + 1 + shift

                    if not stack:
                        if len(wrong_seq) > 1:
                            break
                        wrong_seq.append(ind + 1 + shift)
                        continue

                    stack.pop()

            shift += memory_limit
            input_str = f.readline(memory_limit)

        if len(stack) == 1 and len(wrong_seq) == 0:
            pos = stack.pop()

        if len(wrong_seq) == 1 and len(stack) == 0:
            pos = min_pos

        print(pos)

get_min_pos()
