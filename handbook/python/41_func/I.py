def is_prime(num: int) -> bool:
    if num % 2 == 0:
        return False

    for i in range(3, int(pow(num, 0.5)) + 1, 2):
        if not num % i:
            return False

    return True


def is_prime_native(num: int) -> bool:
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_ferma(num: int) -> bool:
    return (2 << num - 2) % num == 1


if __name__ == '__main__':
    print(is_prime(1001459))
    print(is_prime(79701))
