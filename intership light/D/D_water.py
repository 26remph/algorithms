import sys
import timeit
import time
import statistics
from bisect import bisect_left, bisect_right

from bisect import bisect_left


def find_end(arr: list, ind: int, x: int, left, right) -> int:
    # print('left, right:', left, right)

    if right <= left:
        return right
    mid = (left + right) // 2
    if arr[mid][ind] == x:
        while mid + 1 < len(arr):
            print('-->')
            if arr[mid + 1][ind] == x:
                mid += 1
            else:
                break
        return mid
    elif x < arr[mid][ind]:
        return find_end(arr, ind, x, left, mid)
    else:
        return find_end(arr, ind, x, mid + 1, right)


def binsearch(arr: list, ind: int, x: int, left, right) -> int:
    # print('binary, left, right:', left, right)

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

start_time = time.time()

# data = read_input()
data = read_data_file('data_create.txt')
print('data_size_of:', sys.getsizeof(data))
print("READ: --- %s seconds ---" % (time.time() - start_time))


start_ind = sorted(data, key=lambda x: (x[0], x[1]))
keys_x0 = [x[0] for x in start_ind]
sum = 0
start_sum = []
for row in start_ind:
    sum += row[2]
    start_sum.append(sum)
# print('start_sum', start_ind)
# print('start_sum', start_sum)

end_ind = sorted(data, key=lambda x: (x[1], x[0]))
keys_x1 = [x[1] for x in end_ind]
end_sum = []
sum = 0
for row in end_ind:
    sum += row[1] - row[0]
    end_sum.append(sum)
# print('end_ind:', end_ind)
# print('end_sum:', end_sum)
print("SORTED: --- %s seconds ---" % (time.time() - start_time))

qtime = []
with open('query.txt') as f:
    # q = int(input())
    q = f.readline().rstrip()
    while line := f.readline().rstrip():
    # for _ in range(q):
    #     row = list(map(int, input().split()))
        query_time = time.time()

        row = list(map(int, line.split()))
        start, end, _type = row

        source = end_ind if _type == 2 else start_ind
        search_ind = 1 if _type == 2 else 0
        keys = keys_x1 if _type == 2 else keys_x0

        bi_time_start = time.time()
        ind = binsearch(source, search_ind, start, 0, len(source))
        ind_end = find_end(source, search_ind, end, 0, len(source))

        ind_bi = bisect_left(keys, start)
        print('query:', start, end, _type)
        print('source:', source)
        print('ind, ind_bi;', ind, ind_bi)
        print('selected_keys:', keys)
        print('keys_x0', keys_x0)
        print('keys_x1', keys_x1)
        assert ind == ind_bi
        bi_time_end = time.time()

        _sum_alt = 0

        sub_query_start = time.time()
        _sum = 0
        for pos in range(ind, len(source)):

            if source[pos][search_ind] > end:
                break

            if _type == 2:
                _sum += source[pos][1] - source[pos][0]
            else:
                _sum += source[pos][2]
        sub_query_end = time.time()

        # print('_sum, _sum_alt:', _sum, _sum_alt)
        # assert _sum == _sum_alt

        # print(
        #     # _sum,
        #     f'QT --- {str((time.time() - query_time) * 1000)}  ms --- '
        #     f'bi, {(bi_time_end - bi_time_start) * 1000} --'
        #     f'sub_q, {(sub_query_end - sub_query_start) * 1000} ---'
        # )
        # qtime.append((time.time() - query_time) * 1000)
        # print("QUERY: --- %s seconds ---" % (time.time() - start_time))

# print("TOTAL: --- %s seconds ---" % (time.time() - start_time))
# print(f"COUNT: --- {len(qtime)}")
# print(f"AVG TIME QUERY: --- {statistics.mean(qtime)}")
