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
        total_sum = end_sum if _type == 2 else start_sum

        bi_time_start = time.time()
        # ind = binsearch(source, search_ind, start, 0, len(source))
        edge = len(source) - 1
        # edge = -10
        # ind_end = find_end(source, search_ind, end, 0, len(source))

        ind_left = bisect_left(keys, start)
        # if ind_left == len(keys):
        #     ind_left = 0
        ind_right = bisect_right(keys, end)
        if ind_right:
            ind_right -= 1

        # print('\nquery:', start, end, _type)
        # print('source:', source)
        # print('total_sum', total_sum)
        # print('search_ind', search_ind)
        # print('ind, ind_left;', ind, ind_left)
        # print('selected_keys:', keys)
        # print('keys_x0', keys_x0)
        # print('keys_x1', keys_x1)
        # assert ind == ind_left

        _sum_alt = 0
        # if (source[0][search_ind] <= end) and (ind_left <= ind_right):
        #     _sum_alt = total_sum[0]

        if ind_left <= ind_right and len(source) == 1:
            if source[0][search_ind] <= end:
                _sum_alt = total_sum[0]

        if ind_left <= ind_right and len(source) > 1:
            if ind_left - 1 < 0:
                _sum_alt = total_sum[ind_right]
            else:
                _sum_alt = total_sum[ind_right] - total_sum[ind_left - 1]
        bi_time_end = time.time()

        sub_query_start = time.time()
        _sum = 0
        flag = False
        # for pos in range(ind, len(source)):
        #
        #     if source[pos][search_ind] > end:
        #         flag = True
        #         break
        #
        #     if _type == 2:
        #         _sum += source[pos][1] - source[pos][0]
        #     else:
        #         _sum += source[pos][2]
        sub_query_end = time.time()
        # edge = pos

        # if flag:
        #     edge = max(0, pos - 1)

        # print('edge_ind, ind_right:', edge, ind_right)

        # assert edge == ind_right
        # print('_sum, _sum_alt:', _sum, _sum_alt)
        # assert _sum == _sum_alt

        print(
            # _sum,
            f'QT --- {str((time.time() - query_time) * 1000)}  ms --- '
            f'bi, {(bi_time_end - bi_time_start) * 1000} --'
            # f'sub_q, {(sub_query_end - sub_query_start) * 1000} ---'
        )
        qtime.append((time.time() - query_time) * 1000)
        # print("QUERY: --- %s seconds ---" % (time.time() - start_time))

print("\nTOTAL: --- %s seconds ---" % (time.time() - start_time))
print(f"COUNT: --- {len(qtime)}")
print(f"AVG TIME QUERY: --- {statistics.mean(qtime)}")
