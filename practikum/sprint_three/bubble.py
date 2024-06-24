
def get_bubble(n, arr):
    f = False
    is_printed = False
    while not f:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f = True
        if f:
            f = False
            is_printed = True
            print(*arr)
        else:
            f = True

        if not is_printed:
            print(*arr)


n = int(input())
arr = list(map(int, input().split(' ')))
get_bubble(n, arr)
