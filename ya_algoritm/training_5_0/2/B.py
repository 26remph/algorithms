

def main():

    ans = [0]
    st, end = 0, K if len(arr) != K else K - 1

    while end < len(arr):
        min_price = (arr[st], st)  # (price, day)
        max_price = (arr[st], st)  # (price, day)
        for d in range(st, end + 1):
            if min_price[0] > arr[d]:
                min_price = arr[d], d
            if max_price[0] <= arr[d] and min_price[1] <= d:
                max_price = arr[d], d
        if min_price[1] < max_price[1]:
            ans.append(max_price[0] - min_price[0])

        st += 1
        end += 1

    # print(ans)
    return max(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(main())

    # max_t = 0
    # for _ in range(100):
    #     N, K = 10_000, random.randint(1, 100)
    #     arr = [random.randint(1, 10_000) for _ in range(N)]
    #     t = timeit.timeit(main, number=1)
    #     max_t = max(max_t, t)
    # print(max_t)
