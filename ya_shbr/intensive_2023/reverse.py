def insert_selection(arr):

    for i in range(len(arr) - 1, -1, -1):
        maxel = arr[0], 0
        for j in range(0, i):
            if arr[j] > maxel[0]:
                maxel = arr[j], j

        arr[i], arr[maxel[1]] = arr[maxel[1]], arr[i]

    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    print(arr)


if __name__ == '__main__':
    arr = [1, 7, 8, 9, 10, 11, 3]
    insert_selection(arr)