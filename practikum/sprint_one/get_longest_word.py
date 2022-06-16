def get_longest_word(line: str) -> str:
    if not line:
        return line

    lines = line.split()
    rez = sorted(lines, key=lambda x: (-len(x), lines.index(x)))[0]
    return rez

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))