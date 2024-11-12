def is_power_of_four(number: int) -> bool:
    n: int = 0
    while True:
        rez = pow(4, n)
        if rez == number:
            return True

        if rez > number:
            return False

        n += 1


print(is_power_of_four(int(input())))
