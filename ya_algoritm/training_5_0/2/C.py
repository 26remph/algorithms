if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    x = max(arr)
    y = sum(arr) - x
    if y < x:
        print(x - y)
    else:
        print(sum(arr))

    # print(x, y)