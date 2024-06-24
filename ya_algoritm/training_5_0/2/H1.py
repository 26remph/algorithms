from copy import deepcopy


def set_row_to_zero(a: list, row: int):
    a[row] = [0 for _ in range(m + 1)]
    a[0] = [0 for _ in range(m + 1)]


def set_column_to_zero(a: list, column: int):
    # set max to zero
    for i in range(n + 1):
        a[i][column] = 0
        a[i][0] = 0


def renew_max_for_column():

    # search new max for j
    max_column = [0, 0]
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            arr[0][j] = max(arr[0][j], arr[i][j])
            if max_column[0] < arr[i][j]:
                max_column[0] = arr[i][j]
                max_column[1] = j

    return max_column


def renew_max_for_row(a: list) -> list:

    # search new max for i
    max_row = [0, 0]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][0] = max(a[i][j], a[i][0])
            if max_row[0] < a[i][j]:
                max_row[0] = a[i][j]
                max_row[1] = i
    return max_row


def get_max(a: list):
    left_max = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left_max = max(left_max, a[i][j])
    return left_max


if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = [[0 for _ in range(m + 1)] for _ in range(1)]
    max_i, max_j = [0, 0], [0, 0]
    for i in range(1, n + 1):
        ai = list(map(int, input().split()))
        arr.append([0] + ai)
        for j in range(1, len(ai) + 1):
            arr[0][j] = max(arr[0][j], ai[j - 1])
            arr[i][0] = max(arr[i][0], ai[j - 1])
            if arr[0][j] > max_j[0]:
                max_j[0], max_j[1] = arr[0][j], j

        if arr[i][0] > max_i[0]:
            max_i[0], max_i[1] = arr[i][0], i

    # calculate second array
    arr_copy = deepcopy(arr)
    set_column_to_zero(arr_copy, max_j[1])
    new_max_i = renew_max_for_row(arr_copy)
    set_row_to_zero(arr_copy, new_max_i[1])
    left_max = get_max(arr_copy)
    res_2 = (new_max_i[1], max_j[1], left_max)

    # calculate first arr
    set_row_to_zero(arr, max_i[1])
    new_max_j = renew_max_for_column(arr)
    set_column_to_zero(arr, new_max_j[1])
    left_max = get_max(arr)
    res_1 = (max_i[1], new_max_j[1], left_max)  # (i, j, left_max)

    ans = (res_1[0], res_1[1]) if res_1[2] <= res_2[2] else (res_2[0], res_2[1])
    print(' '.join(map(str, ans)))
