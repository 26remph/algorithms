def main():
    n = int(input())
    i = 0
    while n >= i:
        n -= i
        i += 1

    return i - 1


if __name__ == '__main__':
    print(main())
