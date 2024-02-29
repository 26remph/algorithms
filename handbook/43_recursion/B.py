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
    # print(recursive_digit_sum(100))
    #
    # for _ in range(10_000_000):
    #     summ = 0
    #     num = random.randint(1, 1_000_000)
    #     assert recursive_digit_sum(num) == sum(map(int, str(num))), num

    for i in range(1_000_000_000):
        assert int(i % 10) == i % 10 and int(i / 10) == i // 10, i
