d = {
    0: 0,
    1: 1,
    2: 2,
    3: 2,
    4: 1
}


def main():
    col = 0
    for _ in range(int(input())):
        ai = int(input())
        col += ai // 4 + d[ai % 4]

    return col


if __name__ == '__main__':
    print(main())
