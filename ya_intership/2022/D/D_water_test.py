import sys
import time

from bisect import bisect_left, bisect_right


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
data = read_data_file("data_create.txt")
print("READ: --- %s seconds ---" % (time.time() - start_time))

start_ind = sorted(data, key=lambda x: (x[0], x[1]))
keys_x0 = [x[0] for x in start_ind]
sum = 0
start_sum = []
for row in start_ind:
    sum += row[2]
    start_sum.append(sum)

end_ind = sorted(data, key=lambda x: (x[1], x[0]))
keys_x1 = [x[1] for x in end_ind]
end_sum = []
sum = 0
for row in end_ind:
    sum += row[1] - row[0]
    end_sum.append(sum)
print("SORTED: --- %s seconds ---" % (time.time() - start_time))


with open("query.txt") as f:
    # q = int(input())
    q = f.readline().rstrip()
    while line := f.readline().rstrip():
        row = list(map(int, line.split()))
        start, end, _type = row

        source = end_ind if _type == 2 else start_ind
        search_ind = 1 if _type == 2 else 0
        keys = keys_x1 if _type == 2 else keys_x0
        total_sum = end_sum if _type == 2 else start_sum

        ind_left = bisect_left(keys, start)
        # if ind_left == len(keys):
        #     ind_left = 0

        ind_right = bisect_right(keys, end)
        if ind_right:
            ind_right -= 1

        _sum_alt = 0
        if ind_left <= ind_right and len(source) == 1 and source[0][search_ind] <= end:
                _sum_alt = total_sum[0]

        if ind_left <= ind_right and len(source) > 1:
            if ind_left - 1 < 0:
                _sum_alt = total_sum[ind_right]
            else:
                _sum_alt = total_sum[ind_right] - total_sum[ind_left - 1]

        print(_sum_alt)

print("\nTOTAL: --- %s seconds ---" % (time.time() - start_time))
print(
    "data_size_of:",
    sys.getsizeof(data)
    + sys.getsizeof(start_ind)
    + sys.getsizeof(keys_x0)
    + sys.getsizeof(end_ind)
    + sys.getsizeof(keys_x1),
)
