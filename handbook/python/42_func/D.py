import datetime
import locale


d = {"мая": "Май"}


def month_loc(num: int, loc="ru") -> str:
    name = locale.normalize(loc)
    locale.setlocale(locale.LC_TIME, name)
    m = datetime.datetime.strptime(str(num), "%m").strftime("%B")
    if d.get(m):
        return d[m]

    if loc == "ru":
        last_char = m[-1:]
        m = str(m[:-1] + "ь") if last_char == "я" else m[:-1]
        return m.capitalize()

    return m.capitalize()


d: dict[int, str] = {
    1: ("январь", "january"),
    2: ("февраль", "february"),
    3: ("март", "march"),
    4: ("апрель", "april"),
    5: ("май", "may"),
    6: ("июнь", "june"),
    7: ("июль", "july"),
    8: ("август", "august"),
    9: ("сентябрь", "september"),
    10: ("октябрь", "october"),
    11: ("ноябрь", "november"),
    12: ("декабрь", "december"),
}


def month(num: int, loc="ru") -> str:
    ind = 0 if loc == "ru" else 1
    if d.get(num):
        return d.get(num, "")[ind].capitalize()


if __name__ == "__main__":
    print(month(1, "en"))
    print(month(7))
    print(month(13))
