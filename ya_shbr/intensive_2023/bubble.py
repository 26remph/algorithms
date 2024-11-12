def solution(arr):
    while True:
        flag = True
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                flag = False

        if flag:
            break

    print(arr, flag)


if __name__ == "__main__":
    arr = [9, 8, 7, 8, 9, 0, 8]
    solution(arr)
