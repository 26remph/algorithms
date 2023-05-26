from collections import Counter


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    count = Counter(arr)

    cnt = 0
    for _, val in count.items():
        if val == 1:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
