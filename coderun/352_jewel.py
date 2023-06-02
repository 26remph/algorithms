

def main():
    J = set(input())
    S = input()

    cnt = 0
    for ch in S:
        if ch in J: cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()