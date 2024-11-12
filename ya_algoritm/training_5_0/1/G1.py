def check_win(i, j):
    # i, j = 16, 26
    # i, j = 37, 60
    # i, j = 61, 99
    # i, j = 80, 99
    # i, j = 82, 133
    step = 1
    while i > 0 and j > 0:
        # print(f'{step},{(i, j)}')
        buffer.add((i, j))
        i, j = j - i, i
        step += 1

    # print(bool(step % 2))
    return bool(step % 2)


def cash():
    for i in range(1, 1000):
        for j in range(i, 1000):
            if j / i > 1.625:
                check_win(i, j)


def main():
    cnt = 0
    total = 0
    for i in range(1, 5000):
        for j in range(i, 5000):
            if j / i > 1.625:
                total += 1
                if (i, j) in buffer:
                    cnt += 1

    print("hit", cnt, "form", total, cnt / total * 100)


if __name__ == "__main__":
    buffer = set()
    cash()
    main()
    # print(timeit.timeit('main()', number=1, globals=globals()))
    print(max(buffer), min(buffer), len(buffer))
