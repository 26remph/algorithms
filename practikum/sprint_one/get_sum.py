import time

from typing import Tuple


def get_sum(f_num: str, s_num: str) -> str:
    max_digit: int = max(len(f_num), len(s_num)) + 1
    shift_digits: int = 0

    for _ in range(max_digit - len(f_num)):
        f_num = '0' + f_num

    for _ in range(max_digit - len(s_num)):
        s_num = '0' + s_num

    rez_str: str = ''
    for dig in range(max_digit - 1, -1, -1):

        bit_sum = int(f_num[dig]) + int(s_num[dig]) + shift_digits
        shift_digits = 0

        if bit_sum == 3:
            shift_digits = 1
            bit_sum = 1

        if bit_sum == 2:
            shift_digits = 1
            bit_sum = 0

        if dig == 0 and bit_sum == 0:
            continue

        rez_str = str(bit_sum) + rez_str

    return rez_str


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()

start_time = time.time()
print(get_sum(first_number, second_number))
print("--- %s seconds ---" % (time.time() - start_time))
