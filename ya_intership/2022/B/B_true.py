id_time = {}

n = int(input())
for _ in range(n):
    log_data = input().split()
    x = id_time.setdefault(int(log_data[3]), [])
    x.append((
        (int(log_data[0]) * 1440) + (int(log_data[1]) * 60) + (int(log_data[2])),
        log_data[4],
    ))

for ship, ship_time in id_time.items():
    ship_time = sorted(ship_time)
    id_time[ship] = int(
        sum(
            (ship_time[i + 1][0] - ship_time[i][0])
            for i in range(len(ship_time) - 1)
            if ship_time[i + 1][1] != "A"
        )
    )

print(*(value for _, value in sorted(id_time.items())))
