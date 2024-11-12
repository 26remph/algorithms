import random
import time


data_dict = {}
data_list = []
N = 200_000
EDGE = 1_000_000_000

for ind in range(N):
    data_dict[ind] = (
        random.randint(1, EDGE),
        random.randint(1, EDGE),
        random.randint(1, EDGE),
    )

for _ in range(N):
    data_list.append((
        random.randint(1, EDGE),
        random.randint(1, EDGE),
        random.randint(1, EDGE),
    ))

# start_time = time.time()
# for _ in range(N):
#     ind = random.randint(0, N - 1)
#     x = data_dict[ind]
#     rez = x[0] * x[1]
# print("DICT TIME: --- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
for _ in range(N):
    ind = random.randint(0, N - 1)
    for i in range(ind, N - 1):
        if i < N - 1:
            x = data_list[ind]
            rez = x[0] * x[1]

print("LIST TIME: --- %s seconds ---" % (time.time() - start_time))
