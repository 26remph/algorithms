import sys
import timeit

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


def read_input() -> list:

    n = int(input())

    data = []
    for _ in range(n):
        data.append(tuple(map(int, input().split())))

    return data

def read_data_file(filename):

    data = []
    with open(filename) as f:
        f.readline()
        while line := f.readline().rstrip():
            data.append(tuple(map(int, line.split())))

    return data


# data = read_input()
data = read_data_file('data_create.txt')
print('data_size_of:', sys.getsizeof(data))


start_ind = sorted(data, key=lambda x: (x[0], x[1]))
end_ind = sorted(data, key=lambda x: (x[1], x[0]))


with open('query.txt') as f:
    # q = int(input())
    q = f.readline().rstrip()
    while line := f.readline().rstrip():
    # for _ in range(q):
    #     row = list(map(int, input().split()))
        row = list(map(int, line.split()))
        start, end, _type = row

        source = end_ind if _type == 2 else start_ind

        search_ind = 1 if _type == 2 else 0
        ind = binsearch(source, search_ind, start, 0, len(source))

        _sum = 0
        for pos in range(ind, len(source)):

            if source[pos][search_ind] > end:
                break

            if _type == 2:
                _sum += source[pos][1] - source[pos][0]
            else:
                _sum += source[pos][2]

        print(_sum)
