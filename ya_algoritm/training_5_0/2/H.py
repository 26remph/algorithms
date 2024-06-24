import random

from copy import deepcopy


def test_func(ta):
    del ta[0]
    for i in range(n):
        ta[i] = ta[i][1:]
    print(ta)

    test_ans = []
    min_max = [float('inf'), -1, -1]
    for i in range(n):
        for j in range(m):
            copy_test = deepcopy(ta)
            for k in range(n):
                for l in range(m):
                    if k == i or l == j:
                        copy_test[k][l] = 0

            print('---')
            max_copy = 0
            for k in range(n):
                for l in range(m):
                    max_copy = max(copy_test[k][l], max_copy)
            if max_copy <= min_max[0]:
                min_max[0] = max_copy
                min_max[1] = i + 1
                min_max[2] = j + 1
                test_ans.append(min_max[:])
            for k in copy_test:
                print(k)
            print(max_copy)
    print(f'min_max: {min_max}')
    print(f'{test_ans=}')
    result = set()
    for i in range(len(test_ans)):
        if test_ans[i][0] == min_max[0]:
            result.add((test_ans[i][1], test_ans[i][2]))

    print(f'{result=}')
    return result


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

    # n, m = map(int, input().split())
    # arr = [[0 for _ in range(m+1)] for _ in range(1)]
    # max_i, max_j = [0, 0], [0, 0]
    # for i in range(1, n+1):
    #     ai = list(map(int, input().split()))
    #     arr.append([0] + ai)
    #     for j in range(1, len(ai) + 1):
    #         arr[0][j] = max(arr[0][j], ai[j - 1])
    #         arr[i][0] = max(arr[i][0], ai[j - 1])
    #         if arr[0][j] > max_j[0]:
    #             max_j[0], max_j[1] = arr[0][j], j
    #
    #     if arr[i][0] > max_i[0]:
    #         max_i[0], max_i[1] = arr[i][0], i

    while True:
        n, m = random.randint(2, 10), random.randint(2, 10)
        arr = [[0 for _ in range(m + 1)] for _ in range(1)]
        max_i, max_j = [0, 0], [0, 0]
        for i in range(1, n + 1):
            # ai = list(map(int, input().split()))
            ai = [random.randint(1, 100) for _ in range(m)]
            arr.append([0] + ai)
            for j in range(1, len(ai) + 1):
                arr[0][j] = max(arr[0][j], ai[j - 1])
                arr[i][0] = max(arr[i][0], ai[j - 1])
                if arr[0][j] > max_j[0]:
                    max_j[0], max_j[1] = arr[0][j], j

            if arr[i][0] > max_i[0]:
                max_i[0], max_i[1] = arr[i][0], i

        test_arr = deepcopy(arr)
        test_ans = test_func(test_arr)

        # debug
        print('\ninit')
        for i in range(n + 1):
            print(arr[i])

        print('\nsecond convert')
        # calculate second array
        arr_copy = deepcopy(arr)
        set_column_to_zero(arr_copy, max_j[1])
        new_max_i = renew_max_for_row(arr_copy)
        set_row_to_zero(arr_copy, new_max_i[1])
        left_max = get_max(arr_copy)
        res_2 = (new_max_i[1], max_j[1], left_max)
        print('second:', f'{max_i=}, {max_j=}, {new_max_i=}, {left_max=}, {res_2=}')
        for i in range(n + 1):
            print(arr_copy[i])

        # calculate first arr
        set_row_to_zero(arr, max_i[1])
        new_max_j = renew_max_for_column(arr)
        set_column_to_zero(arr, new_max_j[1])
        left_max = get_max(arr)
        res_1 = (max_i[1], new_max_j[1], left_max)  # (i, j, left_max)
        print('first:', f'{max_i=}, {max_j=}, {new_max_j=}, {left_max=}, {res_1=}')

        ans = (res_1[0], res_1[1]) if res_1[2] <= res_2[2] else (res_2[0], res_2[1])
        for i in range(n + 1):
            print(arr[i])
        print(f'{test_ans=}, {ans=}')
        assert ans in test_ans
        # print(' '.join(map(str, ans)))
