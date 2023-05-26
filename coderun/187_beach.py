
def main():
    # T = int(input())
    # for t in range(T):
    #     n = int(input())
    #     arr = list(map(int, input().split()))
    #
    #     min_ = arr[0] ^ arr[1]
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             min_ = min(arr[i] ^ arr[j], min_)
    #
    #     print(min_)

    arr = [2, 4, 5, 8]
    print(2 ^ 4, 2 ^ 5, 2 ^ 8)
    print(4 ^ 5, 4 ^ 8)
    print(5 ^ 8)


if __name__ == '__main__':
    main()