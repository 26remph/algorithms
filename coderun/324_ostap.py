def main():
    N, M = map(int, input().split())

    bid = list(map(int, input().split()))
    ask = list(map(int, input().split()))

    bid.sort()
    ask.sort(reverse=True)

    n = min(N, M)

    profit = 0
    for i in range(n):
        if ask[i] > bid[i]:
            profit += ask[i] - bid[i]

    print(profit)


if __name__ == "__main__":
    main()
