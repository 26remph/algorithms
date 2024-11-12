from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    set_s: set = set(shorter)
    set_l: set = set(longer)
    if set_s != set_l:
        return "".join(map(str, set_l - set_s))

    rez: str = ""
    for x in set_s:
        if longer.count(x) != shorter.count(x):
            rez = x
            break

    return rez


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
