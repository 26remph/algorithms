def binsearch(arr: list, ind: int, x: int, left, right) -> int:
    if right <= left:
        return right
    mid = (left + right) // 2
    if arr[mid][ind] == x:
        while mid - 1 >= 0:
            if arr[mid - 1][ind] == x:
                mid -= 1
            else:
                break
        return mid
    elif x < arr[mid][ind]:
        return binsearch(arr, ind, x, left, mid)
    else:
        return binsearch(arr, ind, x, mid + 1, right)


def water():
    with open("data_create.txt") as f:
        # n = int(input())
        _ = int(f.readline().rstrip())
        data = []
        while line := f.readline().rstrip():
            data.append(tuple(map(int, line.split())))

        start_ind = sorted(data, key=lambda x: (x[0], x[1]))
        end_ind = sorted(data, key=lambda x: (x[1], x[0]))

    print(end_ind)
    with open("query.txt") as f:
        # q = int(input())
        _ = int(f.readline().rstrip())

        rez = []
        while line := f.readline().rstrip():
            row = list(map(int, line.split()))
            start, end, _type = row

            source = end_ind if _type == 2 else start_ind

            search_ind = 1 if _type == 2 else 0
            ind = binsearch(source, search_ind, start, 0, len(source))

            sum_day = 0
            for pos in range(ind, len(source)):
                if source[pos][search_ind] > end:
                    break

                if _type == 2:
                    sum_day += source[pos][1] - source[pos][0]
                else:
                    sum_day += source[pos][2]

            rez.append(str(sum_day))
            # print(sum_day)

    # print(''.join(rez))
    return "".join(rez)
