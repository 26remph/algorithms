def main(_, holiday):
    calendar = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    if year % 400 == 0 or year % 4 == 0 and year % 100:
        calendar["February"] = 29

    day_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    total = [0 for _ in range(len(day_of_week))]

    pos = [k for k, v in day_of_week.items() if v == start_day][0]
    for key, val in calendar.items():
        for d in range(1, val + 1):
            if (str(d), key) in holiday:
                total[pos] -= 1
            else:
                total[pos] += 1

            # print(
            #   f'{key=}, {pos=},{day_of_week[pos]}, {total=},
            #   {(str(d), day_of_week[pos])=}'
            # )
            pos += 1
            pos = pos % 7

    max_d = 0
    min_d = 0
    for i in range(len(total)):
        if total[max_d] < total[i]:
            max_d = i
        if total[min_d] > total[i]:
            min_d = i

    # print(f'{total=}')
    return f"{day_of_week[max_d]} {day_of_week[min_d]}"


if __name__ == "__main__":
    n = int(input())
    year = int(input())
    holiday = {tuple(input().split()) for _ in range(n)}
    start_day = input()
    print(main(year, holiday))
