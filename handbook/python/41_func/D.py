import datetime
import locale


d: dict[str, tuple[str, ...]] = {
    'en': (
        'january', 'february', 'march',
        'april', 'may', 'june',
        'july', 'august', 'september',
        'october', 'november', 'december'
    ),
    'ru': (
        'январь', 'февраль', 'март',
        'апрель', 'май', 'июнь',
        'июль', 'август', 'сентябрь',
        'октябрь', 'ноябрь', 'декабрь'
    )
}


def month_ext(m: int, lng: str) -> str:
    lst_month = d.get(lng, ())
    name_month = lst_month[m - 1].capitalize()
    return name_month.capitalize()


def month(m: int, lng: str) -> str:
    d = {'мая': 'Май'}
    loc_name = locale.normalize(lng)
    locale.setlocale(locale.LC_TIME, loc_name)
    dt = datetime.datetime.strptime(str(m), "%m")

    normalize = d.get(dt.strftime("%B"))
    if normalize:
        return normalize

    last_char = dt.strftime("%B")[-1:]
    if last_char == 'а':
        return dt.strftime('%B')[:-1].capitalize()

    if last_char == 'я':
        return str(dt.strftime('%B')[:-1] + 'ь').capitalize()

    return dt.strftime('%B').capitalize()


if __name__ == '__main__':
    print([month(i, 'en') for i in range(1, 13)])
    print([month(i, 'ru') for i in range(1, 13)])
