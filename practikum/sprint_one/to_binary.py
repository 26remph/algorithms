def to_binary(number: int) -> str:
    if number == 0:
        return "0"

    bin_digits = []

    while number != 1:
        digit = number % 2
        bin_digits.append(digit)
        number = (number - 1) // 2 if digit == 1 else number // 2

    bin_digits.append(1)

    return "".join(str(x) for x in reversed(bin_digits))


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
