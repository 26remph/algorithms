ship_time = {}

for _ in range(int(input())):
    log_data = input().split()
    ship_time.setdefault(int(log_data[3]), []).append(
        (
            (int(log_data[0]) * 1440) + (int(log_data[1]) * 60) + (
                int(log_data[2])),
            log_data[4],
        )
    )

for ship, ship_data in ship_time.items():
    ship_data = sorted(ship_data)
    ship_time[ship] = int(
        sum(
            (ship_data[i + 1][0] - ship_data[i][0])
            for i in range(len(ship_data) - 1)
            if ship_data[i + 1][1] != "A"
        )
    )

print(*(v for k, v in sorted(ship_time.items())))