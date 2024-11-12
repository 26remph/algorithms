from typing import Generator


def cycle(arr: list) -> Generator[int, None, None]:
    pos = -1
    while True:
        pos = (pos + 1) % len(arr)
        yield arr[pos]


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]), strict=False)))
print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]), strict=False)))
