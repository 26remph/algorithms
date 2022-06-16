from typing import List

def min_simple(n: int) -> int:
    if n % 2 == 0:
        return 2

    i = 3
    while n % i != 0 and i * i <= n:
        i += 2

    return i if i * i <= n else n


def factorize(number: int) -> List[int]:
    rez: list = []
    mul: int = 1
    cur_number: int = number

    while mul != number:
        min_spl = min_simple(cur_number)
        mul = mul * min_spl
        rez.append(min_spl)
        cur_number = cur_number // min_spl

    return rez


result = factorize(int(input()))
print(" ".join(map(str, result)))

