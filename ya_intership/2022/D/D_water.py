from bisect import bisect_left, bisect_right


def read_input() -> list:

    with open('data_create.txt') as f:

        # n = int(input())
        n = int(f.readline().rstrip())

        data = []
        while line := f.readline().rstrip():
        # for _ in range(n):
        #     data.append(tuple(map(int, input().split())))
            data.append(tuple(map(int, line.split())))

    return data


def water():
    data = read_input()
    start_ind = sorted(data, key=lambda x: (x[0], x[1]))
    keys_x0 = [x[0] for x in start_ind]
    _sum = 0
    start_sum = []
    for row in start_ind:
        _sum += row[2]
        start_sum.append(_sum)

    end_ind = sorted(data, key=lambda x: (x[1], x[0]))
    keys_x1 = [x[1] for x in end_ind]
    end_sum = []
    _sum = 0
    for row in end_ind:
        _sum += row[1] - row[0]
        end_sum.append(_sum)

    print(end_ind)
    with open('query.txt') as f:
        # q = int(input())
        q = int(f.readline().rstrip())
        rez = []
        while line := f.readline().rstrip():
        # for _ in range(q):
        #     row = list(map(int, input().split()))
            row = list(map(int, line.split()))
            start, end, _type = row

            source = end_ind if _type == 2 else start_ind
            search_ind = 1 if _type == 2 else 0
            keys = keys_x1 if _type == 2 else keys_x0
            total_sum = end_sum if _type == 2 else start_sum

            ind_left = bisect_left(keys, start)

            ind_right = bisect_right(keys, end)
            if ind_right:
                ind_right -= 1

            _sum_alt = 0
            if ind_left <= ind_right and len(source) == 1:
                if source[0][search_ind] <= end:
                    _sum_alt = total_sum[0]

            if ind_left <= ind_right and len(source) > 1:
                if ind_left - 1 < 0:
                    if source[ind_right][search_ind] <= end:
                        _sum_alt = total_sum[ind_right]
                else:
                    _sum_alt = total_sum[ind_right] - total_sum[ind_left - 1]

            rez.append(str(_sum_alt))
            print('ind_left:', ind_left)
            print('ind_right:', ind_right)
            print('_sum_alt:', _sum_alt)
            # print(_sum_alt)
    return ''.join(rez)

# print(' '.join(rez))
