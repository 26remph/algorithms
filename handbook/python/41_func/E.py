def split_numbers(s: str) -> tuple[int, ...]:
    return tuple(map(int, s.split()))


if __name__ == "__main__":
    print(split_numbers("1 2 3 4 5"))
    print(split_numbers("1 -2 3 -4 5"))
