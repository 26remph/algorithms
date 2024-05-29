import random


def recursive_digit_sum(n: int, summa=0):
    if n:
        summa += n % 10
        return recursive_digit_sum(n // 10, summa)

    return summa


def recursive_digit_sum_ex(n: int, summa=0):
    if n:
        summa += int(n % 10)
        return recursive_digit_sum(int(n / 10), summa)

    return summa


if __name__ == '__main__':
    print(recursive_digit_sum(123))
    print(recursive_digit_sum(7321346))

