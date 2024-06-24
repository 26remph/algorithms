import random

import D_water as dw_speed
import D_water_TL as dw_tl


MODE = {
    False: 'data_create',
    True: 'query'
}
RIGHT_EDGE = 100
MAX_DATA_INTERVAL = 100
MAX_QUERY_INTERVAL = 1_000


def create_test():

    # mode = bool(int(input('Mode data create (0) - data, (1) - query\n')))
    mode = bool(0)
    n = MAX_DATA_INTERVAL

    with open(f'{MODE.get(mode)}.txt', 'w') as f:
        f.write(str(n))

        for _ in range(n):
            start = random.randint(1, RIGHT_EDGE)
            end = random.randint(start, RIGHT_EDGE)

            param = random.randint(1, 2) if mode else random.randint(1, RIGHT_EDGE)

            f.write(f'\n{start} {end} {param}')

    mode = bool(1)
    n = MAX_QUERY_INTERVAL

    with open(f'{MODE.get(mode)}.txt', 'w') as f:
        f.write(str(n))

        for _ in range(n):
            start = random.randint(1, RIGHT_EDGE)
            end = random.randint(start, RIGHT_EDGE)

            param = random.randint(1, 2) if mode else random.randint(1, RIGHT_EDGE)

            f.write(f'\n{start} {end} {param}')


# create_test()
rez_1 = dw_speed.water()
print(rez_1)
rez_2 = dw_tl.water()
print(rez_2)
for i in range(len(rez_1)):
    if rez_1[i] != rez_2[i]:
        print('diff_pos:', i)
        print(rez_1[i], rez_2[i])

assert rez_1 == rez_2
