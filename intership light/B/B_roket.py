from datetime import datetime, timedelta


def flight_time(num_day: int, start: str, end: str) -> int:
    frm = '%H:%M'
    t1 = datetime.strptime(start, frm)
    t2 = datetime.strptime(end, frm)

    t_delta = t2 - t1
    if t_delta.days < 0:
        t_delta = timedelta(days=0, seconds=t_delta.seconds)
        if num_day > 0:
            num_day -= 1

    print('\ntime_delta:', t_delta, timedelta(num_day))
    print('time_delta sec:', t_delta.seconds)
    print('num_day', num_day)
    print('rez:', t_delta.seconds // 60 + num_day * 3600)
    return t_delta.seconds // 60 + num_day * 3600


n = int(input())

data_vector = []
for _ in range(n):
    data = input().split()
    data_vector.append(
        (int(data[3]), int(data[0]), data[4], data[1], data[2])
    )

data_vector.sort(key=lambda x: (x[0], x[1], x[2]))
print(data_vector)

id = data_vector[0][0]
stat_A = (data_vector[0][1], f'{data_vector[0][3]}:{data_vector[0][4]}')
end_BC = None

i = 1

while i < len(data_vector):

    fl_time = 0
    while i < len(data_vector) and id == data_vector[i][0]:

        if data_vector[i][2] == 'A':
            stat_A = (data_vector[i][1], f'{data_vector[i][3]}:{data_vector[i][4]}')

        if data_vector[i][2] in ('S', 'C'):
            end_BC = (data_vector[i][1], f'{data_vector[i][3]}:{data_vector[i][4]}')
            fl_time += flight_time(end_BC[0] - stat_A[0], stat_A[1], end_BC[1])

        i += 1

    print('fl_time:', id, fl_time)

    if i < len(data_vector):
        id = data_vector[i][0]
        # stat_A = (data_vector[i][1], f'{data_vector[i][3]}:{data_vector[i][4]}')
        # end_BC = None


